from django.urls import path
from .import views
from .views import afficher_menu ,  commande_view, home_view, view_confirmation
 

urlpatterns = [
    path('', home_view, name='home'),  # URL racine redirige vers le menu
    path('menu/', afficher_menu, name='menu'),
    path('commande/<int:plat_id>/', commande_view, name='commande'),
    path('confirmation',view_confirmation, name='confirmation'),
]
    
