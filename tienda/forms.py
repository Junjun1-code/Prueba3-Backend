from django import forms
from .models import Item , Rating

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemname', 'price', 'published', 'img']
        widgets = {
            'itemname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el nombre de tu artículo a vender'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Escribe el precio aquí...'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'img': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa la URL de la imagen del producto...'
            })
        }
        labels = {
            'itemname': 'Nombre del articulo',
            'price': 'Valor',
            'published': '¿Publicar artículo?',
            'img': 'Imagen'
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars','comments']
        widgets = {
            # 'rateditem': (attrs={
            #     'placeholder': (f'{rateditem}')
            # })

            'stars': forms.Select(
                choices=[
                    ('', '¿Como calificas este producto?'),
                    (1, '1 ⭐'),
                    (2, '2 ⭐⭐'),
                    (3, '3 ⭐⭐⭐'),
                    (4, '4 ⭐⭐⭐⭐'),
                    (5, '5 ⭐⭐⭐⭐⭐'),
                ],    
                attrs={
                    'class': 'form-select',
                }),

            'comments': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Agrega comentarios sobre el producto'
            }),
        }
        labels = {
            'stars': 'Calificación',
            'comments': 'Comentario'
        }
