from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render (request,'Bloodbank_admin/admin_home.html')
def donors(request):
    return render (request,'Bloodbank_admin/donors.html')
def patients(request):
    return render (request,'Bloodbank_admin/patients.html')
def change_password(request):
    return render (request,'Bloodbank_admin/change_password.html')
def approve_donors(request):
    return render (request,'Bloodbank_admin/approve_donors.html')
def blood_stock(request):
    return render (request,'Bloodbank_admin/blood_stock.html')
def request_history(request):
    return render (request,'Bloodbank_admin/request_history.html')
