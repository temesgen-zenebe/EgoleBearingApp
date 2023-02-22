from django.urls import path
from .import views

app_name = 'orders'

urlpatterns = [
    path('orders', views.OrderCreate, name='OrderCreate'),
    path('orders/admin_detail/<int:order_id>', views.AdminOrderDetail, name='AdminOrderDetail'),
    path('orders/admin_pdf/<int:order_id>', views.AdminOrderPDF, name='AdminOrderPDF')
]
