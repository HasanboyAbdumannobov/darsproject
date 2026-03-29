from django.contrib import admin
from .models import Category, Product, Order, OrderProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_editable = ('category',)
    list_filter = ('category',)
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    
    
admin.site.register(Product)