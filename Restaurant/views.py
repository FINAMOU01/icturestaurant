
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Menu ,commande
from Restaurant .models import Plat 
from .forms import commandeForm
from django.contrib import messages


def home_view(request):
    return redirect('menu')

def afficher_menu(request):
    menus = Menu.objects.all()
    return render(request, 'restaurant/menu.html', {'menus': menus})

def commande_view(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)

    if request.method == 'POST':
        form = commandeForm(request.POST)
        print(form.errors)  # Affiche les erreurs du formulaire
        if form.is_valid():
            quantite = form.cleaned_data['quantite']
            if request.POST.get('action') == 'cancel':
                # L'utilisateur a cliqué sur le bouton "Annuler"
                messages.info(request, 'command cancelled.')
                return redirect('menu')
            if plat.disponible >= quantite:
             #reserver le plat
             commande.objects.create(
                plat=plat,
                nom_client=form.cleaned_data['nom_client'],
                email_client=form.cleaned_data['email_client'],
                quantite=form.cleaned_data['quantite'],
                heure_disponibilite=heure_disponibilite,
                mode_paiement=mode_paiement 
             )
            
             plat.disponible -= quantite
             plat.save()
             messages.success(request, 'Order successful!')
             return redirect('menu')
            else:
                messages.error(request, 'Apologies,but your order has been declined due to eceeding the maximum allowed number of plates (5 plats)')
    else:
        form = commandeForm()

    return render(request, 'commande.html', {'form': form, 'plat': plat})