from django.urls import path

from .views import(
    HomePageView,
    AboutUsView, 
    ContactUsView,
    TermsPolicesView,
    SellerDashboardView,
    SellerProductView,
    DashboardView, 
    )

app_name = 'pages'

urlpatterns = [
  
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'), 
    path('terms-polices/', TermsPolicesView.as_view(), name='terms-polices'), 
    path('seller-dashboard/', SellerDashboardView.as_view(), name='seller_Dashboard'),
    path('seller-product/', SellerProductView.as_view(), name='seller_product'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
]