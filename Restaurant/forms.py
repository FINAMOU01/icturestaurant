from django import forms
from PIL import Image
from django.core.exceptions import ValidationError

def validate_heure_disponibilite(time):
    if time.hour < 8 or time.hour > 16:
        raise ValidationError("the pickup time should be between 8:00 AM and 4:00 PM")


class commandeForm(forms.Form):
    quantite = forms.IntegerField(min_value=1, label='Quantite')
    nom_client = forms.CharField(max_length=100, required=True)
    email_client = forms.EmailField(required=True)
    heure_disponibilite = forms.TimeField(
        label='Choose your preferred pickup time',
        input_formats=['%I:%M %p'],
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'step': '300'
        }),
        validators=[validate_heure_disponibilite]
    )
    deposit_receipt = forms.ImageField(
        label="Click here to download deposit receipt image :",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        }),
        required=True,
        validators=[]
    )       

    @staticmethod
    def validate_image_file(file):
        try:
            img = Image.open(file)
            img.verify()
        except IOError:
            raise forms.ValidationError("Invalid image file")

    validators = [validate_image_file]