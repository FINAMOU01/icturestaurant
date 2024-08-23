from django import forms
class commandeForm(forms.Form):
    quantite = forms.IntegerField(min_value=1, label='Quantite')
    nom_client = forms.CharField(max_length=100, required=True)
    email_client = forms.EmailField(required=True)
    mode_paiement = forms.CharField(label='MODES_PAIEMENT')