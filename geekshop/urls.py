from django.urls import path
from django.contrib import admin
import products.views as products
from users.views import login, register, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', products.main, name='main'),
    path('products/', products.products, name='products'),
    path('contact/', products.contact, name='contacts'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
