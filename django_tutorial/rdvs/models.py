from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Lieu(models.Model):
    nom=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.address}'

class Participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Rdv(models.Model):
    auteur=models.ForeignKey(User,on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    email_organisateur=models.EmailField()
    date=models.DateField()
    slug=models.SlugField(unique=True)
    description=models.TextField()
    #image=models.ImageField(upload_to='images')
    lieu=models.ForeignKey(Lieu, on_delete=models.CASCADE)
    participants=models.ManyToManyField(Participant, blank=True,null=True)
   

    def save(self):
        self.slug=slugify(self.titre)
        super(Rdv,self).save()

    def __str__(self):
        return f'{self.titre}'
