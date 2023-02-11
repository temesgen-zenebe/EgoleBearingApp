from django.db import models
from common.utils.text import unique_slug , create_new_ref_number
from django.db import models
import barcode   # additional imports
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from common.utils.text import unique_slug
from django.urls import reverse
from django.utils import timezone
import random
import string

# Create your models here.
#product
#brand
#category
#store_branch
#images
#specification
#seller
#buyer

class Brand(models.Model):
    brand = models.CharField(max_length=100 ,null=True, blank=True)
    made_in = models.CharField(max_length=100,null=True, blank=True)
    specification = models.CharField(max_length=100, null=True, blank=True)
    manufactured = models.CharField(max_length=100,blank=True ,null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
     
    class Meta:
        ordering = [ '-created']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
    
    
    def __str__(self): 
        return str(f'{self.brand}-{self.made_in}')

class Category(models.Model):
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    
     
    class Meta:
        ordering = [ '-created']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self) 
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
    
    def __str__(self): 
        return self.category

class Images(models.Model):
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image6 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    alt = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    
     
    class Meta:
        ordering = [ '-created']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.alt) 
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
            
    def __str__(self): 
        return str(self.alt)

class Specification(models.Model):
    specifications_code = models.CharField(max_length = 10,blank=True,editable=False,unique=True,default=create_new_ref_number)
    instruction = models.CharField(max_length=600,blank=True, null=True)
    warning = models.CharField(max_length=600,blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    diminution = models.CharField(max_length=100,blank=True, null=True)
    weight =  models.CharField(max_length=100,blank=True, null=True)
    color = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=100,blank=True, null=True)
    industry = models.CharField(max_length=100,blank=True, null=True)
    application = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
     
    class Meta:
        ordering = [ '-created']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
    
    def __str__(self): 
        return str(self.specifications_code)

class Store_branch(models.Model):
    suppliers = models.CharField(max_length=100,blank=True, null=True)
    store_name = models.CharField(max_length=100,blank=True, null=True)
    branch = models.PositiveSmallIntegerField(blank=True, null=True)
    location = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    contact = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    class Meta:
        ordering = [ '-created']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
    
    def __str__(self): 
        return str(f'{self.store_name}-{self.branch}')
    
class products(models.Model):
    TAGS = ( (None, '--Please choose--'),('sell', 'sell'),('Hot', 'Hot'),('Fast moving', 'Fast moving'), )
    LABEL = ((None, '--Please choose--'),('Bast seller', 'Bast seller'), ('AutoZoom Choice', 'AutoZoom Choice'),('New', 'New'),)
    RETURN_POLICE=((None, '--Please choose--'),('No Return', 'No Return'),('same day', 'same day'),('seven days', 'seven days')
                   ,('Fifteen(15) days', 'Fifteen(15) days'),('Thirty(30) days', 'Thirty(30) days'),)
    SHIPPING = ( (None, '--Please choose--'),('Free', 'Free'),('Not Free', 'Not Free')
                ,('on Stor pickup', 'on Stor pickup'),('Buy 5+ get one free', 'Buy 5+ get one free')
                ,('let you know on checkout', 'let you know on checkout'), )
    STATES = ( (None, '--Please choose--'),('new brand', 'new brand'),('Open box', 'Open box')
                ,('used', 'used'),('like New', 'like new'),)
    suppliers = models.CharField(max_length=300,blank=True, null=True)
    stores = models.ForeignKey(Store_branch , on_delete=models.CASCADE,blank=True ,null=True)
    product_name = models.CharField(max_length=300,blank=True, null=True)
    part_number = models.CharField(max_length=200 ,blank=False , null=False)
    cost =  models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount =  models.PositiveSmallIntegerField(default=1)
    quantity = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE,blank=True ,null=True)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE,blank=True ,null=True)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=600,blank=True ,null=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    tags = models.CharField(max_length=30, choices=TAGS,blank=True, null=True)
    label = models.CharField(max_length=30, choices=LABEL, blank=True, null=True)
    return_police = models.CharField(max_length=30, choices=RETURN_POLICE, blank=True, null=True)
    states = models.CharField(max_length=30, choices=STATES, blank=True, null=True)
    available = models.BooleanField(default=True)
    shipping = models.CharField(max_length=30, choices=SHIPPING, blank=True, null=True)
    images = models.ForeignKey(Images, on_delete=models.PROTECT, blank=True, null=True)
    shelf_no = models.PositiveSmallIntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=50, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    class Meta:
        ordering = [ '-created']
    
    def get_absolute_url(self):
      return reverse('product:detail', args=[self.slug])
    
    def createdDate(self):
        self.created = timezone.now()
        self.save()
    
    def save(self, *args, **kwargs):          # overriding save() 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.product_name}-{self.part_number}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.product_name}-{self.part_number}.png', File(rv), save=False)
        #slug
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
   
    def __str__(self): 
        return str(f'{self.product_name}-{self.part_number}')


