from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(
        ('Children','Children'),
        ('Parents','Parents'),
        ('GYM','GYM')
    )
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True,choices= CATEGORY)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

# Create your models here.
