from django.urls import path
from . import views

urlpatterns = [
    # LIST
    path('', views.item_list, name='list_items'),
    # DETAIL
    path('item/<int:pk>/', views.item_detail, name='detail_items'),
    # CREATE
    path('item/new/', views.item_post, name='post_items'),
    # UPDATE
    path('item/<int:pk>/edit/', views.item_edit, name='edit_items'),
    # DELETE
    path('item/<int:pk>/remove/', views.item_remove, name='remove_items'),

    # LIST
    path('', views.rating_list, name='list_ratings'),
    # DETAIL
    path('articulo/<int:pk>/', views.rating_detail, name='detail_ratings'),
    # CREATE
    path('articulo/nuevo/', views.rating_post, name='make_ratings'),
    # UPDATE
    path('articulo/<int:pk>/editar/', views.rating_edit, name='edit_ratings'),
    # DELETE
    path('articulo/<int:pk>/eliminar/', views.rating_remove, name='remove_ratings'),
]
