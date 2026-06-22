from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item
from .forms import ItemForm, RatingForm

# ++ Articulos para el catalogo ++++++++++++++++++++++++

# ── LIST: Ver todos los artículos ────────────────────────────────────────────
def item_list(request):
    """Página pública: muestra artículos publicados. 
       Si el usuario está autenticado, también ve los suyos sin publicar."""
    if request.user.is_authenticated:
        items = Item.objects.filter(author=request.user)
    items = Item.objects.filter(published=True)
    return render(request, 'tienda/items.html', {'Items': items})

# ── DETAIL: Ver un artículo ────────────────────────────────────────────────
def item_detail(request, pk):
    Item = get_object_or_404(Item, pk=pk)
    # Solo el autor puede ver sus artículos no publicados
    if not Item.published and Item.author != request.user:
        messages.error(request, 'Este artículo no está disponible.')
        return redirect('list_items')
    
    # Ratings = get_object_or_404(Ratings, fk=pk )
    # return render(request, 'blog/detalle.html', {'Item': Item, 'Ratings': Ratings })
    
    return render(request, 'tienda/detalle.html', {'Item': Item})

# ── CREATE: Crear artículo ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def item_post(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item = form.save(commit=False)  # no guarda aún en BD
            Item.autor = request.user       # asigna el usuario actual
            Item.save()
            messages.success(request, '¡Artículo creado exitosamente!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = ItemForm()
    return render(request, 'tienda/form.html', {'form': form, 'accion': 'Crear'})
# ── UPDATE: Editar artículo ────────────────────────────────────────────────
@login_required
def item_edit(request, pk):
    Item = get_object_or_404(Item, pk=pk, author=request.user)  # solo el autor puede editar
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = ItemForm(instance=Item)
    return render(request, 'tienda/form.html', {'form': form, 'accion': 'Editar', 'Item': Item})

# ── DELETE: Eliminar artículo ──────────────────────────────────────────────
@login_required
def item_remove(request, pk):
    Item = get_object_or_404(Item, pk=pk, author=request.user)
    if request.method == 'POST':
        Item.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('lista_Items')
    return render(request, 'tienda/confirmar_eliminar.html', {'Item': Item})


# ++ Valoraciones de los articulos +++++++++++++++++++++++++++++++

# # # ── LIST: Ver todos los artículos ────────────────────────────────────────────
# def rating_list(request, pk):
#     Item = get_object_or_404(Item, pk=pk)

#     return render(request, 'tienda/items.html',)

# # def rating_list(request):
# #     """Página pública: muestra artículos publicados. 
# #        Si el usuario está autenticado, también ve los suyos sin publicar."""
# #     if request.user.is_authenticated:
# #         items = Item.objects.filter(author=request.user)
# #     items = Item.objects.filter(published=True)
# #     return render(request, 'blog/lista.html', {'Items': items})


# ── CREATE: Crear valoracion ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def rating_post(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            Item = form.save(commit=False)  # no guarda aún en BD
            Item.autor = request.user       # asigna el usuario actual
            Item.pk += request.pk           # asigna el articulo a valorar
            Item.save()
            messages.success(request, '¡Artículo valorado exitosamente!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = RatingForm()
    return render(request, 'tienda/form.html', {'form': form, 'accion': 'Crear'})

# # ── UPDATE: Editar valoracion ────────────────────────────────────────────────
# @login_required
# def rating_edit(request, pk):
#     Rating = get_object_or_404(Rating, pk=pk, author=request.user)  # solo el autor puede editar
#     if request.method == 'POST':
#         form = RatingForm(request.POST, instance=Rating)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '¡Artículo actualizado!')
#             return redirect('detalle_Item', pk=Item.pk)
#     else:
#         form = RatingForm(instance=Item)
#     return render(request, 'tienda/form.html', {'form': form, 'accion': 'Editar', 'Item': Item})

# ── DELETE: Eliminar valoracuib ──────────────────────────────────────────────
@login_required
def rating_remove(request, pk):
    Rating = get_object_or_404(Rating, pk=pk, autor=request.user)
    if request.method == 'POST':
        Rating.delete()
        messages.success(request, 'Valoracion eliminada.')
        return redirect('lista_Items')
    return render(request, 'tienda/confirmar_eliminar.html', {'Valoración': Rating})
