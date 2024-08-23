from django.urls import path
from .views import afficher_menu ,  commande_view, home_view
 

urlpatterns = [
    path('', home_view, name='home'),  # URL racine redirige vers le menu
    path('menu/', afficher_menu, name='menu'),
    path('commande/<int:plat_id>/', commande_view, name='commande'),
]
    
