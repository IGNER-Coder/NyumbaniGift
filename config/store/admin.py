from django.contrib import admin
from .models import Category, Product

# 1. Register the Category Model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Auto-fills the slug as you type the name

# 2. Register the Product Model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'created_at', 'updated_at']
    list_filter = ['in_stock', 'category'] # Adds a sidebar filter
    list_editable = ['price', 'in_stock'] # Allows you to edit price/stock directly in the list view!
    prepopulated_fields = {'slug': ('name',)}