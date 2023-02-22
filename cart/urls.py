from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('cart/cartList/', views.cartList, name='carList'),
    path('cart/cartUpdate/<slug:slug>/', views.CartUpdate, name='cartUpdate'),
    path('cart/cartRemove/<slug:slug>/', views.CartRemove, name='cartRemove'),
    path('cartAdd', views.cartAdd, name='cartAdd'),
]
