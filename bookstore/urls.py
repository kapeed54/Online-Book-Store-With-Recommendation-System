from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('about/',include('about.urls')),
    path('accounts/',include('accounts.urls')),
    path('contact/',include('contact.urls')),
    path('',include('shop.urls', namespace="shop")),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
