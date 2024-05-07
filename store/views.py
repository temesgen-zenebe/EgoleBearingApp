from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import products,Category,Specification,Store_branch,Brand,Images
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import Q


# class ProductListView(View):
#     def get(self, request):
#         # Initial product list rendering
#         products_list = products.objects.all().order_by('-created')
#         # Handle category filtering
#         category = request.GET.get('category')
#         if category:
#             products_list = products_list.filter(category__category=category)
#         return render(request, 'store/products_list.html', {'products_list': products_list})

#     def post(self, request):
#         # Handle advanced filtering form submission
#         category = request.POST.get('category')
#         brand = request.POST.get('brand')
#         search_query = request.POST.get('search')
#         filtered_products_list = products.objects.all()
#         if category:
#             filtered_products_list = filtered_products_list.filter(category__category=category)
#         if brand:
#             filtered_products_list = filtered_products_list.filter(brand__brand=brand)
#         if search_query:
#             filtered_products_list = filtered_products_list.filter(Q(part_number__icontains=search_query) | Q(product_name__icontains=search_query))
#         return render(request, 'store/product_list_partial.html', {'products_list': filtered_products_list})


   
class ProductsList(ListView):
   
    # specify the model for list view
    model = products
    context_object_name = "products_list" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = products.objects.all() 
        context['product_brand'] = {}

        for item in product:
            brand = item.brand.brand
            if brand not in context['product_brand']:
                context['product_brand'][brand] = Brand.objects.filter(brand=brand)
        return context


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
    fields = ['brand','made_in', 'logo', 'manufactured']
    template_name = 'pages/seller/add_product_brand.html'
    success_url = "/seller/products/" 
    
    def form_valid(self, form):
        messages.success(self.request, "The product Brand was created successfully.")
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