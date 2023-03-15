from django.db import models

# Create your models here.


class Product(models.Model):
    TYPE_CHOICES = [
        ('em', 'Emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conservé')
    ]

    label = models.CharField(max_length=100)
    description = models.TextField(default='Non defini')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(
        'Categorie', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.label} ({self.type}): {self.price} DT"


class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor')
    ]
    name = models.CharField(
        max_length=50, default='Alimentaire', choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(default='Non defini')
    email = models.EmailField(default='Non defini')
    telephone = models.CharField(max_length=8)
    Fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)
