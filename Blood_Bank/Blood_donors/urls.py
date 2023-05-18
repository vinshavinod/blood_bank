from django.urls import path
from .import views

app_name= 'Blood_donors'

urlpatterns=[
    path('donor_home',views.donor_home, name='donor_home'),
    path('blooddonor_registration',views.blooddonor_registration, name='blooddonor_registration'),
    path('login',views.login, name='login'),
    path('change_password',views.change_password, name='change_password'),
    path('blood_list',views.blood_list, name='blood_list'),
    path('view_profile',views.view_profile, name='view_profile'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
]