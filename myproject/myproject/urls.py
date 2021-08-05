"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splitscreen),
    path('add-product/<str:restaurant_name>', addproduct, name='addproduct'),
    path('customer-login', customer_login),
    path('customer-register', customer_register),
    path('restaurant-login', restaurant_login),
    path('restaurant-register', restaurant_register),
    path('customer-logout', customer_logout),
    path('restaurant-logout', restaurant_logout),
    path('restaurants', all_restaurants, name='view_restaurants'),
    path('menu/<str:restaurant_name>/<str:username>', menu, name='menu'),
    path('cart/<str:username>', cart, name='cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
