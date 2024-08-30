from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
#class plat
class Plat(models.Model):
    nom=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.DecimalField(max_digits=6, decimal_places=0)
    disponible=models.BooleanField(default=True)
    image = models.ImageField(upload_to='plats/')
    
   

    def __str__(self):
        return self.nom
  #class menu  
    
class Menu(models.Model):
    nom=models.CharField(max_length=100)
    plats=models.ManyToManyField(Plat)
    def __str__(self):
        return self.nom

   #class de commande 

class commande(models.Model):
    STATUT_CHOICES = [
        ('pending', 'Pending'),
        ('validated', 'Validated'),
        ('delivered', 'Delivered'),
        ('cancelled','Cancelled'),
    ]
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    nom_client = models.CharField(max_length=100 ,default='client')
    email_client = models.EmailField(default='unknow@example.com')
    date_commande = models.DateTimeField(auto_now_add=True)
    heure_disponibilite = models.TimeField(default=timezone.now().time())
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES,default='en_attente')
    deposit_receipt = models.ImageField(upload_to='receipts/', null=True, blank=True)

    def __str__(self):
        return f"order of {self.quantite} x {self.plat.nom} by {self.nom_client}"

    