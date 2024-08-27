from django.contrib import admin
from .models import Plat, Menu ,commande
# Register your models here.
admin.site.site_header = "ICTURESTAURANT"
admin.site.site_title = "SBC Restaurant"
admin.site.index_title ="Manager" 


class DishAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'image' )
    fields = ('nom', 'description','prix', 'image')
    list_editable=('prix',)

    search_fields = ('nom',)
class commandeAdmin(admin.ModelAdmin):
    list_display = ('nom_client','email_client', 'plat','quantite', 'date_commande', 'heure_disponibilite','statut','deposit_receipt')
    fields=('nom_client','email_client', 'plat','quantite', 'date_commande', 'heure_disponibilite','statut','deposit_receipt')
    search_fields = ('nom_client',)
    list_editable =('statut',)

admin.site.register(Plat, DishAdmin)
admin.site.register(Menu)
admin.site.register(commande, commandeAdmin )
