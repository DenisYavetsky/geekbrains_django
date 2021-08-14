from django.urls import path
from django.contrib import admin
import products.views as products

urlpatterns = [
    path('', products.main),
    path('products/', products.products),
    path('contact/', products.contact),
    path('admin/', admin.site.urls),
]