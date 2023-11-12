"""agromart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from agromarkethub import views, AdminViews, ConsumerViews, SellerViews
from django.conf.urls.static import static

from agromart import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard', AdminViews.admin_dashboard),
    path('all_orders', AdminViews.all_orders),
    path('all_sellers', AdminViews.all_sellers),
    path('consumer_home', ConsumerViews.home),
    path('become_a_seller', ConsumerViews.become_a_seller),
    path('do_seller_register', ConsumerViews.do_seller_register),
    path('seller_dashboard', SellerViews.home),
    path('add_produce', SellerViews.add_produce),
    path('do_add_produce', SellerViews.do_add_produce),
    path('', views.showLoginPage),
    path('login', views.doLogin),
    path('register', views.showRegisterPage),
    path('do_register', views.doRegister),
    path('get_user_details', views.getUserDetails),
    path('logout', views.logoutUser),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)