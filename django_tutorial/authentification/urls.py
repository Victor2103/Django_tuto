from django.shortcuts import redirect
from django.urls import  path 
from . import views

urlpatterns=[
    path('sign_up',views.sinscrire,name='sinscrire'),
    path('',views.home,name='home')
]