from django.contrib import admin
from .models import Order, OrderItem

# This creates a mini-table of items INSIDE the Order page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'paid', 'created']
    list_filter = ['paid', 'created', 'city']
    inlines = [OrderItemInline] # Connects the items to the order