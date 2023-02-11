
from django.contrib import admin  
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User Management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),
   

    path('', include('pages.urls')),
    path('', include('store.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 