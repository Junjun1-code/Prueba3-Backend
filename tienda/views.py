from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item , Rating
from .forms import ItemForm , RatingForm
from django.db.models import Avg

# ++ Articulos para el catalogo ++++++++++++++++++++++++

# ── LIST: Ver todos los artículos ────────────────────────────────────────────
def item_list(request):
    """Página pública: muestra artículos publicados. 
       Si el usuario está autenticado, también ve los suyos sin publicar."""
    if request.user.is_authenticated:
        items = Item.objects.filter(author=request.user) | Item.objects.filter(published=True)
    else:
        items = Item.objects.filter(published=True)
    return render(request, 'tienda/item.html', {'Item': items})

# ── DETAIL: Ver un artículo ────────────────────────────────────────────────
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Solo el autor puede ver sus artículos no publicados
    if not item.published and item.author != request.user:
        messages.error(request, 'Este artículo no está disponible.')
        return redirect('list_items')

    ratings = Rating.objects.filter(rateditem=item)
    for rating in ratings:
        rating.star_range = range(rating.stars)

    return render(request, 'tienda/item_detail.html', {'Item': item, 'Ratings': ratings})

# ── CREATE: Crear artículo ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def item_post(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item = form.save(commit=False)  # no guarda aún en BD
            Item.author = request.user       # asigna el usuario actual
            Item.save()
            messages.success(request, '¡Artículo creado exitosamente!')
            return redirect('detail_items', pk=Item.pk)
    else:
        form = ItemForm()
    return render(request, 'tienda/item_form.html', {'form': form, 'accion': 'Crear'})
# ── UPDATE: Editar artículo ────────────────────────────────────────────────
@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk, author=request.user)  # solo el autor puede editar
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado!')
            return redirect('detail_items', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'tienda/item_form.html', {'form': form, 'accion': 'Editar', 'Item': item})

# ── DELETE: Eliminar artículo ──────────────────────────────────────────────
@login_required
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk, author=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('list_items')
    return render(request, 'tienda/remove_confirm_item.html', {'Item': item})


# # ++ Valoraciones de los articulos +++++++++++++++++++++++++++++++

# # ── LIST: Obtener todas las valoraciones ────────────────────────────────────────────


# ── CREATE: Crear valoracion ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def rating_post(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating = form.save(commit=False)  # no guarda aún en BD
            Rating.rateditem = item
            Rating.author = request.user       # asigna el usuario actual
            Rating.save()
            messages.success(request, '¡Artículo valorado exitosamente!')
            return redirect('detail_items', pk=item.pk)
    else:
        form = RatingForm()
    return render(request, 'tienda/rating_form.html', {'form': form, 'accion': 'Crear', 'Item': item})

# # ── UPDATE: Editar valoracion ────────────────────────────────────────────────
@login_required
def rating_edit(request, pk):
    Rating = get_object_or_404(Rating, pk=pk, author=request.user)  # solo el autor puede editar
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=Rating)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = RatingForm(instance=Item)
    return render(request, 'tienda/rating_form.html', {'form': form, 'accion': 'Editar', 'Item': Item})

# ── DELETE: Eliminar valoracuib ──────────────────────────────────────────────
@login_required
def rating_remove(request, pk):
    Rating = get_object_or_404(Rating, pk=pk, autor=request.user)
    if request.method == 'POST':
        Rating.delete()
        messages.success(request, 'Valoracion eliminada.')
        return redirect('lista_Items')
    return render(request, 'tienda/remove_confirm_rating.html', {'Ratings': Rating})
