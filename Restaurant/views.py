
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
        form = commandeForm(request.POST, request.FILES)
        print(form.errors)  # Affiche les erreurs du formulaire
        if form.is_valid():
            quantite = form.cleaned_data['quantite']
            receipt = form.cleaned_data.get('deposit_receipt')
            print("Receipt:", receipt)
            if request.POST.get('action') == 'cancel':
                # L'utilisateur a cliqué sur le bouton "Annuler"
                messages.info(request, 'command cancelled.')
                return redirect('menu')
            if quantite <= 5:
             #reserver le plat
                 commande.objects.create(
                   plat=plat,
                   nom_client=form.cleaned_data['nom_client'],
                   email_client=form.cleaned_data['email_client'],
                   heure_disponibilite=form.cleaned_data['heure_disponibilite'],
                   quantite=quantite,
                   deposit_receipt=receipt
             
                )
                 plat.save()
                 messages.success(request, 'Order successful!')
                 return redirect('confirmation')
            
            else:

                messages.error(request, 'Apologies,but your order has been declined due to eceeding the maximum allowed number of plates (5 plates)')
    else:
        form = commandeForm()

    return render(request, 'commande.html', {'form': form, 'plat': plat})
def view_confirmation(request):
    info = commande.objects.all()
    for item in info:
        nom=item.nom_client
    return render(request, 'confirmation.html' ,{'name':nom})



