from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, "consumer_templates/consumer_home_template.html")

def become_a_seller(request):
    return render(request, "consumer_templates/become_a_seller.html")

def do_seller_register(request):
    name = request.POST.get("name_of_establishment")
    address = request.POST.get("address_of_establishment")
    email = request.POST.get("email_address_of_establishment")
    password = request.POST.get("password")

    user = CustomUser.objects.create_user(username=name, email=email, password=password, user_type=2)
    user.seller.address_of_establishment = address
    user.save()
    return HttpResponse("Seller Request Added Successfully, please wait while we review your documents")
    return HttpResponseRedirect("/consumer_home")

