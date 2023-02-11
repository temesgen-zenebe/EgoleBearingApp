from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import products,Category,Specification,Store_branch,Brand,Images
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from django.contrib import messages

   
class ProductsList(ListView):
   
    # specify the model for list view
    model = products
    context_object_name = "products_list" 

class SellerProductsList(ListView):
   
    # specify the model for list view
    model = products
    context_object_name = "List_product" 
    template_name = 'pages/seller/product.html' 

class ProductDetail(DetailView):
    model = products
    template_name = 'store/product_detail.html'
    context_object_name = 'productDetail'

class ProductStockUpdateView(UpdateView): 
	model = products
	fields = [      'stores','product_name','part_number','cost',
                    'price','discount','quantity','category','brand',
                    'specification','description','barcode','tags','label',
                    'return_police','states','available','images','shelf_no'
            ]
   
	success_url ="/seller/products/"
   
#-----------------Delete product---------------- 

class Delete_Product(DeleteView):
    model = products
    success_url ="/seller/products/"
    template_name = "pages/seller/Stack_delete_confirm.html"
    
    def form_valid(self, form):
        messages.success(self.request,"The product Stock Information has been deleted successfully.")
        return super(Delete_Product,self).form_valid(form) 
    
#-----------------Creating new product----------------  

class productStockCreate(CreateView):
    model = products
    fields = ['suppliers','stores','product_name','part_number','cost',
                    'price','discount','quantity','category','brand',
                    'specification','description','barcode','tags','label',
                    'return_police','states','available','images','shelf_no']
    	
    template_name = 'pages/seller/add_product_store.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Information was created successfully.")
        return super(productStockCreate,self).form_valid(form)         

class CategoryCreate(CreateView):
    model = Category
    fields = ['category','sub_category']  	
    template_name = 'pages/seller/add_product_category.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Category was created successfully.")
        return super(CategoryCreate,self).form_valid(form)

class BrandCreate(CreateView):
    model = Brand
    fields = ['brand','made_in','manufactured']
    template_name = 'pages/seller/add_product_brand.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Category was created successfully.")
        return super(BrandCreate,self).form_valid(form)
       
class StoreCreate(CreateView):
    model = Store_branch
    fields = ['suppliers','store_name','branch','location','contact','email','phone'] 
    template_name = 'pages/seller/add_branch_store.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        """ supplier_user = get_object_or_404(Supplier, user = self.request.user)
        form.instance.supplier = supplier_user """
        
        messages.success(self.request, "The product Store was created successfully.")
        return super(StoreCreate,self).form_valid(form) 
          
class SpecificationCreate(CreateView):
    model = Specification
    fields = ['instruction','warning','expiration',
                    'diminution','weight','color','type','industry','application']
    template_name = 'pages/seller/add_product_Specification.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Descriptions was created successfully.")
        return super(SpecificationCreate,self).form_valid(form) 
  
class PictureCreate(CreateView):
    model = Images
    fields = ['image1','image2','image3','image4','image5','image6','alt']
    template_name = 'pages/seller/add_product_picture.html'	
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Images was created successfully.")
        return super(PictureCreate,self).form_valid(form)    