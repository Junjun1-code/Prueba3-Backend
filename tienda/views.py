from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item
from .forms import ItemForm

# ++ Articulos para el catalogo ++++++++++++++++++++++++

# ── LIST: Ver todos los artículos ────────────────────────────────────────────
def Item_list(request):
    """Página pública: muestra artículos publicados. 
       Si el usuario está autenticado, también ve los suyos sin publicar."""
    if request.user.is_authenticated:
        items = Item.objects.filter(author=request.user)
    items = Item.objects.filter(published=True)
    return render(request, 'blog/lista.html', {'Items': items})

# ── DETAIL: Ver un artículo ────────────────────────────────────────────────
def Item_detail(request, pk):
    Item = get_object_or_404(Item, pk=pk)
    # Solo el autor puede ver sus artículos no publicados
    if not Item.published and Item.author != request.user:
        messages.error(request, 'Este artículo no está disponible.')
        return redirect('Items_list')
    
    # Ratings = get_object_or_404(Ratings, fk=pk )
    # return render(request, 'blog/detalle.html', {'Item': Item, 'Ratings': Ratings })
    
    return render(request, 'blog/detalle.html', {'Item': Item})

# ── CREATE: Crear artículo ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def Item_post(request):
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
    return render(request, 'blog/form.html', {'form': form, 'accion': 'Crear'})
# ── UPDATE: Editar artículo ────────────────────────────────────────────────
@login_required
def Item_edit(request, pk):
    Item = get_object_or_404(Item, pk=pk, author=request.user)  # solo el autor puede editar
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = ItemForm(instance=Item)
    return render(request, 'blog/form.html', {'form': form, 'accion': 'Editar', 'Item': Item})

# ── DELETE: Eliminar artículo ──────────────────────────────────────────────
@login_required
def Item_remove(request, pk):
    Item = get_object_or_404(Item, pk=pk, author=request.user)
    if request.method == 'POST':
        Item.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('lista_Items')
    return render(request, 'blog/confirmar_eliminar.html', {'Item': Item})


# ++ Valoraciones de los articulos +++++++++++++++++++++++++++++++

# # ── LIST: Ver todos los artículos ────────────────────────────────────────────
# def Item_list(request):
#     """Página pública: muestra artículos publicados. 
#        Si el usuario está autenticado, también ve los suyos sin publicar."""
#     if request.user.is_authenticated:
#         items = Item.objects.filter(author=request.user)
#     items = Item.objects.filter(published=True)
#     return render(request, 'blog/lista.html', {'Items': items})

# # ── DETAIL: Ver un artículo ────────────────────────────────────────────────
# def Item_detail(request, pk):
#     Item = get_object_or_404(Item, pk=pk)
#     # Solo el autor puede ver sus artículos no publicados
#     if not Item.published and Item.author != request.user:
#         messages.error(request, 'Este artículo no está disponible.')
#         return redirect('Items_list')
#     return render(request, 'blog/detalle.html', {'Item': Item})

# ── CREATE: Crear artículo ────────────────────────────────────────────────
@login_required  # solo usuarios autenticados pueden crear
def Rating_post(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item = form.save(commit=False)  # no guarda aún en BD
            Item.autor = request.user       # asigna el usuario actual
            Item.save()
            messages.success(request, '¡Artículo valorado exitosamente!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = ItemForm()
    return render(request, 'blog/form.html', {'form': form, 'accion': 'Crear'})

# ── UPDATE: Editar artículo ────────────────────────────────────────────────
@login_required
def Rating_edit(request, pk):
    Rating = get_object_or_404(Rating, pk=pk, author=request.user)  # solo el autor puede editar
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo actualizado!')
            return redirect('detalle_Item', pk=Item.pk)
    else:
        form = ItemForm(instance=Item)
    return render(request, 'blog/form.html', {'form': form, 'accion': 'Editar', 'Item': Item})

# ── DELETE: Eliminar artículo ──────────────────────────────────────────────
@login_required
def Item_remove(request, pk):
    Item = get_object_or_404(Item, pk=pk, autor=request.user)
    if request.method == 'POST':
        Item.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('lista_Items')
    return render(request, 'blog/confirmar_eliminar.html', {'Item': Item})
