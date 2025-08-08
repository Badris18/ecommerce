from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']  # Make sure these fields exist
    search_fields = ['name']
    # Only if 'created_at' is a valid model field

admin.site.register(Product, ProductAdmin)
