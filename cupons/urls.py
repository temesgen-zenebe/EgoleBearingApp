from django.urls import path
from . import views

app_name = 'cupons'

urlpatterns = [
    path('cupons/apply/', views.CuponApply, name='apply')
]
