from django.shortcuts import render,redirect
from .forms import InscriptionForm
from django.contrib.auth import login, logout,authenticate


# Create your views here.


def home(request):
    return render(request,'authentification/home.html')

def sinscrire(request):
    if request.method=='POST':
        form=InscriptionForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/touslesrdv/')
    else:
        form=InscriptionForm()
    
    return render(request,'registration/sign-up.html',{"form":form})

    