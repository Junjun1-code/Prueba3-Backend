from django.contrib import admin
from .models import Item , Rating

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['itemname','price','stock','img','published']
    list_filter = ['itemname','published']
    search_fields = ['itemname', 'price']

@admin.register(Rating)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['rateditem','stars']
    list_filter = ['rateditem','author']
    search_fields = ['rateditem','stars']

# Register your models here.
