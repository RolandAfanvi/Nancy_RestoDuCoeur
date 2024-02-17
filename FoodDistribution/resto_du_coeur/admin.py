from django.contrib import admin
from .models import Product,Order,OrderItem,DistributionSite,Category,Stock

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminOrder(admin.ModelAdmin):
    list_display = ['date_order', 'distribution_site', 'get_products']

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])

    get_products.short_description = 'Products'

    
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product','quantity')

class AdminStock(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'last_updated')

class AdminDistributionSite(admin.ModelAdmin):
    list_display = ('name', 'address', 'commune')


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'image', 'stock', 'date_added')


admin.site.register(Product,AdminProduct)
admin.site.register(Order,AdminOrder)
admin.site.register(Category,AdminCategory)
admin.site.register(OrderItem,AdminOrderItem)
admin.site.register(Stock,AdminStock)
admin.site.register(DistributionSite,AdminDistributionSite)