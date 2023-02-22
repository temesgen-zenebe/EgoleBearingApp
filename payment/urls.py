from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment', views.PaymentProcess, name='process'),
    path('payment/done', views.PaymentDone, name='done'),
    path('payment/canceled', views.PaymentCanceled, name='canceled')
]
