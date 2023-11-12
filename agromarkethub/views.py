from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from agromarkethub.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def showRegisterPage(request):
    return render(request, "register.html")

def doRegister(request):
    username = request.POST.get("username")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")
    gender = request.POST.get("gender")
    
    try:
        user=CustomUser.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name,user_type=3)
        user.consumer.address=address
        user.consumer.gender=gender
        user.save()
        return HttpResponseRedirect("/")
    except:
        return HttpResponseRedirect("/register")

def showLoginPage(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_dashboard')
            elif user.user_type == "2":
                return HttpResponseRedirect("/seller_dashboard")
            elif user.user_type == "3":
                return HttpResponseRedirect("/consumer_home")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")