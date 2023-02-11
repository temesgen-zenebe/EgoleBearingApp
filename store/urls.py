from django.urls import path
from .views import (
    ProductsList ,
    ProductDetail, 
    SellerProductsList,
    Delete_Product,
    ProductStockUpdateView,
    productStockCreate,
    CategoryCreate,
    BrandCreate,  
    StoreCreate, 
    SpecificationCreate,
    PictureCreate,
    
    )


app_name = 'store'
urlpatterns = [
    path('products/', ProductsList.as_view(), name='products_list'),
    path('products/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('seller/products/', SellerProductsList.as_view(), name='List_products'),
    path('seller/delete_Product/<slug:slug>', Delete_Product.as_view(), name='delete_Product'),
    path('seller/updated_ProductStock/<slug:slug>/', ProductStockUpdateView.as_view(), name='updated_ProductStock'),
    
    path('seller/add_product/', productStockCreate.as_view(), name='add_productStock'),
    path('seller/add_category/', CategoryCreate.as_view(), name='add_category'),
    path('seller/add_brand/', BrandCreate.as_view(), name='add_brand'),
    path('seller/add_store/', StoreCreate.as_view(), name='add_store'),
    path('seller/add_specification/', SpecificationCreate.as_view(), name='add_specification'), 
    path('seller/add_picture/', PictureCreate.as_view(), name='add_picture'), 
]

