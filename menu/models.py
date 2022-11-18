from django.db import models


class Pizza(models.Model):
    nom = models.CharField(max_length=123)
    prix = models.DecimalField(max_digits=5, decimal_places=2, null=False)


