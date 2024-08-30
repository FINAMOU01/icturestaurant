from django.urls import path
from .import views
from .views import afficher_menu ,  commande_view, view_confirmation
 

urlpatterns = [
    path('menu/', afficher_menu, name='menu'),
    path('commande/<int:plat_id>/', commande_view, name='commande'),
    path('confirmation',view_confirmation, name='confirmation'),
]
    
