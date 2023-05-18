from django.shortcuts import render

# Create your views here.

def user_home(request):
    return render (request,'Blood_users/user_home.html')

def login(request):
    return render (request,'Blood_users/login.html')

def signup(request): 
    return render (request,'Blood_users/signup.html')

def blood_request(request): 
    return render (request,'Blood_users/blood_request.html')

def change_password(request): 
    return render (request,'Blood_users/change_password.html')


