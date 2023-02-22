from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from store.models import products
from cart.models import Cart,CartItem
from .forms import CartAddProductForm 
from cupons.forms import CuponApllyForm


def cartList(request):
    cart = None
    cart_Item = []
    
    if request.user.is_authenticated:
        cart ,created = Cart.objects.get_or_create(user = request.user)
        cart_Item = cart.cart_item.all()
    context = {
        "cart": cart,
        "cart_Item" : cart_Item
    }
    return render(request, 'cart/cartitem/list_cartitems.html' ,context)

def cartAdd(request):
    data = json.loads(request.body)
    product_slug = data["slug"]
    product = products.objects.get(slug = product_slug)
    if request.user.is_authenticated:
        cart ,created = Cart.objects.get_or_create(user = request.user)
        cartItem ,created = CartItem.objects.get_or_create(cart = cart, product = product)
        cartItem.quantity += 1
        cartItem.save()
    return JsonResponse("it is working", safe=False)

def CartRemove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(products, slug=slug)
    cart.remove(product)
    return redirect('cart:CartDetail')

def CartUpdate(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    cupon_apply_form = CuponApllyForm()
    return render(request, 'cart/cartitem/list_cartitems.html',
                 {'cart': cart, 'cupon_apply_form': cupon_apply_form})
