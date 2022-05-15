from django.urls import path 
from . import views

urlpatterns=[
    path('touslesrdv/',views.index,name="tous-rdv"),
    path('seconnecter',views.connexion,name='connexion'),
    path('sign_up',views.sinscrire,name='sinscrire'),
    path('touslesrdv/<slug:rdv_slug>/succes',views.enreg_confirme,name='confirmer-enregistrement'),
    path('touslesrdv/<slug:rdv_slug>',views.plusDetails,name="rdv-details")
]