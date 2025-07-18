from django.contrib import admin
from django.urls import path, include
from Shopping_mall.views import product_list 

urlpatterns = [
    path('', product_list, name='product_list'),  
    path('admin/', admin.site.urls),             
    path('account/', include('accounts.urls')),
    path('shop/', include('Shopping_mall.urls')),
]