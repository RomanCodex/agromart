from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Produce, Order

def add_produce(request):
    return render(request, "seller_templates/add_produce.html")

def do_add_produce(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    category = request.POST.get("category")

    produce = Produce(name=name, seller=1, description=description, price=price, category=category)
    produce.save()
    return HttpResponse("Successfully Added Produce")

def home(request):
    return render(request, "seller_templates/home_content.html")