from django.contrib import admin
from .models import Cart, CartItem 


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['user','transaction_id','completed','slug','created','updated']
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ['cart', 'product','quantity','slug','created','updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()