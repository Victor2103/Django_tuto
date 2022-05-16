from django.contrib import admin

from .models import  Lieu, Participant ,Rdv

# Register your models here.

class RdvAdmin(admin.ModelAdmin):
    list_display= ('titre', 'slug')
    list_filter= ('lieu','date')


admin.site.register(Rdv, RdvAdmin)
admin.site.register(Lieu)
admin.site.register(Participant)
