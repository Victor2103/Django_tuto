from django.contrib import admin

from .models import Rdv, Lieu, Participant

# Register your models here.

class RdvAdmin(admin.ModelAdmin):
    list_display= ('titre', 'slug')
    list_filter= ('lieu','date')
    prepopulated_fields= {'slug':('titre',)}


admin.site.register(Rdv, RdvAdmin)
admin.site.register(Lieu)
admin.site.register(Participant)
