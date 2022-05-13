from xml.etree.ElementInclude import include
from django.urls import path 
from . import views

urlpatterns=[
    path('touslesrdv/',views.index,name="tous-rdv"),
    path('touslesrdv/<slug:rdv_slug>',views.plusDetails,name="rdv-details") 
]