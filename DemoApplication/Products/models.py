from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10000, decimal_places=2)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
