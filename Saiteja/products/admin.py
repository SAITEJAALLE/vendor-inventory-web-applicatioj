from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'vendor')  # Ensure these fields exist
    search_fields = ('name', 'description')  # Searchable fields
    list_filter = ('vendor',)  # Filter by vendor
    readonly_fields = () 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'ordered_at')  # Updated fields
    search_fields = ('product__name', 'user__username')  # Searchable fields
    list_filter = ('product', 'user')  # Filter by product and user

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
