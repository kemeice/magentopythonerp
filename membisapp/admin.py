from django.contrib import admin
from .models import *
# Register your models here.

class MageconnectAdimn (admin.ModelAdmin):
    list_display = ('storeurl', 'key', 'user')
admin.site.register(Mageconnect, MageconnectAdimn )

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Catalog, CatalogAdmin)

class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
admin.site.register(CatalogCategory, CatalogCategoryAdmin)

#class ProductAdmin(admin.ModelAdmin):
   # list_display = ('type_product', 'name', 'description', 'category')
    #prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Product, ProductAdmin)

#class ProductDetailAdmin(admin.ModelAdmin):
    #list_display = ('category', 'product', 'attribute', 'value')
#admin.site.register(ProductDetail, ProductDetailAdmin)


