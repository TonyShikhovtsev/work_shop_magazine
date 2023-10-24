

from django.contrib import admin

from catalog.models import Product, Category

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Product)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'purchase_price', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')