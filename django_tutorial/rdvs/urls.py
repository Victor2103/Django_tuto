from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name="tous-rdv"),
    path('seconnecter',views.connexion,name='connexion'),
    path('<slug:rdv_slug>/succes',views.enreg_confirme,name='confirmer-enregistrement'),
    path('<slug:rdv_slug>',views.plusDetails,name="rdv-details")
]