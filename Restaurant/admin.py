from django.contrib import admin
from .models import Plat, Menu ,commande

class DishAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'image' )
    fields = ('nom', 'description','prix', 'image')

    search_fields = ('name',)


# Register your models here.
admin.site.register(Plat)
admin.site.register(Menu)
admin.site.register(commande)
