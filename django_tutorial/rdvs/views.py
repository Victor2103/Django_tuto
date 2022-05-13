from email.mime import image
from django.shortcuts import render



from .models import Rdv

# Create your views here.



def index(request):
    tousRdv=Rdv.objects.all()
    return render(request,'rdvs/index.html', {
        'keyRdvs':tousRdv
    })

def plusDetails(request,rdv_slug):
    try:
        rdvsdetailles=Rdv.objects.get(slug=rdv_slug)
        return render(request,'rdvs/plus-details.html',{
            'keyRdvTrouve':True,
            'keyRdv':rdvsdetailles
        })
    except Exception as exc:
        return render(request, 'rdvs/plus-details.html',{
            'keyRdvTrouve':False
        })
