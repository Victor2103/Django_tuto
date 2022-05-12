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

def plusDetails(request,rdv_slug):
    print(rdv_slug)
    rdvsdetailles={
        'titre':'un premier rdv',
        'description':'ceci est mon premier rendez vous !'
    }
    
    return render(request,'rdvs/plus-details.html',{
        'keyRdvTitre':rdvsdetailles['titre'],
        'keyRdvDescription':rdvsdetailles['description']
    })
