from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'stock')
    search_fields = ('name', 'short_description')
    list_filter = ('disconunt_until',)
    date_hierarchy = 'disconunt_until'

admin.site.register(Product, ProductAdmin)

