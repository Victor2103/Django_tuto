from django.shortcuts import render

# Create your views here.

def index(request):
    rdvs=[
        {
            'titre': 'un premier rdv',
            'lieu':'Paris',
            'slug':'premier-rdv'
        },
        {
            'titre': 'un deuxième rdv',
            'lieu':'Londres',
            'slug':'deuxieme-rdv'
        }
    ]
    return render(request,'rdvs/index.html', {
        'keyRdvs':rdvs,
        'keyShowRdvs':True
    })
