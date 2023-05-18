from django.urls import path
from .import views

app_name= 'Bloodbank_admin'

urlpatterns=[
    path('admin_home',views.admin_home, name='admin_home'),
    path('donors',views.donors, name='donors'),
    path('patients',views.patients, name='patients'),
    path('change_password',views.change_password, name='change_password'),
    path('approve_donors',views.approve_donors, name='approve_donors'),
    path('blood_stock',views.blood_stock, name='blood_stock'),
    path('request_history',views.request_history, name='request_history'),
]