from django.contrib import admin
from .models import (
        products,
        Brand,
        Category,
        Specification,
        Store_branch,
        Images,
    )

    
@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    model = products
    list_display = ['suppliers','stores','product_name','part_number','cost', 'profit_present',
                    'price','discount_present','off_price','quantity','category','brand',
                    'specification','barcode','tags','label',
                    'return_police','states','available','shipping','images',
                    'shelf_no','slug','created','update']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
        
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ['brand','made_in','logo','manufactured','slug','created','update',]
   
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')

        return ()
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category','sub_category','slug','created','update',]   
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Store_branch)
class Store_branchAdmin(admin.ModelAdmin):
    model = Store_branch
    list_display = ['suppliers','store_name','branch','location',
                    'contact','email','phone','slug',
                    'created','update',] 
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    model = Specification
    list_display = ['specifications_code','instruction','warning','expiration',
                    'diminution','weight','color','type','industry','application',
                    'slug','created','update']
   
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
       
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    model = Images
    list_display = ['image1','image2','image3','image4','image5','image6','alt','slug','created','update']
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
      