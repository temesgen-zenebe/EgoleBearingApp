from django.db import models
from django.conf import settings
from datetime import datetime
from decimal import Decimal
import uuid
from common.utils.text import unique_slug
from django.urls import reverse
from store.models import products

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)
    updated= models.DateField(auto_now=True)
    
    class Meta:
        ordering = [ '-created']
        
        
    def get_absolute_url(self):
      return reverse('cart:detail', args=[self.slug])   
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.transaction_id)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)
        
    def __str__(self):
        return  str(f'{self.transaction_id}-{self.user}')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(products, on_delete=models.CASCADE, related_name ="cart_product")
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
  
    
    class Meta:
        ordering = [ '-created']
    
    def get_absolute_url(self):
      return reverse('cart:detail', args=[self.slug]) 
        
    @property
    def get_subtotal(self):
        return Decimal(self.product.price) * Decimal(self.quantity)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))       
        super().save(*args, **kwargs)

    def __str__(self):
        return  str(self.product)