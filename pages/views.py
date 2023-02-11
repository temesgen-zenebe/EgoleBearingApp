from django.shortcuts import render
from .models import *
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)

  
class HomePageView(TemplateView):
    template_name = 'pages/home.html'
     
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'
    
class TermsPolicesView(TemplateView):
    template_name = 'pages/terms_Polices.html'   


class SellerDashboardView(TemplateView):
    template_name = 'pages/seller_dashboard.html'   
    
class SellerProductView(TemplateView):
    template_name = 'pages/seller/product.html' 
    
class DashboardView(TemplateView):
    template_name = 'pages/seller/dashboard.html'