from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Seller, Order

#Create your views here.
def admin_dashboard(request):
    return render(request, "admin_templates/home_content.html")

def all_orders(request):
    orders = Order.objects.all()
    return render(request, "admin_templates/all_orders.html", {"orders":orders})

def all_sellers(request):
    sellers = Seller.objects.all()
    return render(request, "admin_templates/all_sellers.html", {"sellers":sellers})

def get_pending_sellers(request):
    pass

def approve_seller(request):
    pass

def view_revenue(request):
    pass

def get_statistics(request):
    pass