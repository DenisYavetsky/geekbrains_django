from django.urls import path
from django.contrib import admin
import products.views as products

urlpatterns = [
    path('', products.main, name='main'),
    path('products/', products.products, name='products'),
    path('contact/', products.contact, name='contacts'),
    path('admin/', admin.site.urls),
]