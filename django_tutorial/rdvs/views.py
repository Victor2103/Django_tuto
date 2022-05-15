from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout,authenticate

from .forms import Enregistrement,InscriptionForm



from .models import Rdv,Participant

# Create your views here.



def index(request):
    tousRdv=Rdv.objects.all()
    return render(request,'rdvs/index.html', {
        'keyRdvs':tousRdv
    })

def plusDetails(request,rdv_slug):
    try:
        rdvsdetailles=Rdv.objects.get(slug=rdv_slug)
        if request.method=='GET':
            form_enregistrement=Enregistrement()
        else:
            form_enregistrement=Enregistrement(request.POST)
            if form_enregistrement.is_valid():
                utilisateur_email=form_enregistrement.cleaned_data['email']
                adherent,_=Participant.objects.get_or_create(email=utilisateur_email)
                rdvsdetailles.participants.add(adherent)
                send_mail(
                    "Rendez vous confirmé",
                    "Nous vous confirmons votre rendez vous et d'être inscrit",
                    "vitcheffvi@cy-tech.fr",
                    [utilisateur_email]
                )
                return redirect('confirmer-enregistrement',rdv_slug=rdv_slug)

        return render(request,'rdvs/plus-details.html',{
                'keyRdvTrouve':True,
                'keyRdv':rdvsdetailles,
                'keyFormulaire':form_enregistrement
            })
    except Exception as exc:
        return render(request, 'rdvs/plus-details.html',{
            'keyRdvTrouve':False
        })

def enreg_confirme(request,rdv_slug):
    rdv=Rdv.objects.get(slug=rdv_slug)
    return render(request,'rdvs/enregistrement_reussi.html',{
        'keyOrganisateur':rdv.email_organisateur
    })

def connexion(request):
    return render(request,'rdvs/connexion.html',{})

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

