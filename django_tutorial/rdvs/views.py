from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, Group
from .forms import AjoutRdv, Enregistrement



from .models import Participant , Rdv

# Create your views here.


@login_required(login_url='/login')
def index(request):
    tousRdv=Rdv.objects.all()
    if request.method == 'POST':
        rdvid=request.POST.get('rdv-id')
        userid=request.POST.get('user-id')
        if rdvid:
            rdv=Rdv.objects.filter(id=rdvid).first()
            if rdv and rdv.auteur==request.user or request.user.has_perm("rdvs.delete_rdv"):
                rdv.delete()
        elif userid:
            user=User.objects.filter(id=userid).first()
            if user and request.user.is_staff:
                try:
                    group=Group.objects.get(name='defaut')
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group=Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    return render(request,'rdvs/index.html', {
        'keyRdvs':tousRdv
    })

@login_required(login_url='/login')
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


@login_required(login_url='/login')
def enreg_confirme(request,rdv_slug):
    rdv=Rdv.objects.get(slug=rdv_slug)
    return render(request,'rdvs/enregistrement_reussi.html',{
        'keyOrganisateur':rdv.email_organisateur
    })

@login_required(login_url='/login')
def creer_Rdv(request):
    if request.method=='POST':
        form=AjoutRdv(request.POST)
        if form.is_valid():
            rdv=form.save(commit=False)
            rdv.auteur=request.user
            rdv.email_organisateur=request.user.email
            rdv.save()
            return redirect('/')
    else :
        form=AjoutRdv()

    return render (request, 'rdvs/ajout_rdv.html', {
        "keyForm":form
    })





