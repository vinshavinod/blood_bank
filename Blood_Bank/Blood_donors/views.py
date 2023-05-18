from django.shortcuts import render

# Create your views here.

def donor_home(request):
    return render (request,'Blood_donors/donor_home.html')

def blooddonor_registration(request):
    return render (request,'Blood_donors/blooddonor_registration.html')

def login(request):
    return render (request,'Blood_donors/login.html')

def change_password(request):
    return render (request,'Blood_donors/change_password.html')

def blood_list(request):
    return render (request,'Blood_donors/blood_list.html')

def view_profile(request):
    return render (request,'Blood_donors/view_profile.html')

def edit_profile(request):
    return render (request,'Blood_donors/edit_profile.html')




