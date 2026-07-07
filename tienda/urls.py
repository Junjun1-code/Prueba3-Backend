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

    # CREATE
    path('rating/new/<int:pk>/', views.rating_post, name='post_ratings'),
    # UPDATE
    path('rating/<int:pk>/edit/<int:item_pk>/', views.rating_edit, name='edit_ratings'),
    # DELETE
    path('rating/<int:pk>/remove/<int:item_pk>/', views.rating_remove, name='remove_ratings'),
]
