from django.urls import path
from .import views

app_name= 'Blood_users'

urlpatterns=[
    path('user_home',views.user_home, name='user_home'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('blood_request',views.blood_request, name='blood_request'),
    path('change_password',views.change_password, name='change_password'),
]