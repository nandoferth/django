from django.db import models

# Create your models here.

class customer (models.Model):
  user = models.CharField(max_length=30, null=True)
  email = models.CharField(max_length=50, null=True)
  firstName = models.CharField("person's first name", max_length=30)
  lastName = models.CharField(max_length=30)
  dateCreated = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.user

class product (models.Model):
  SIZES_PRODUCT = (
    ('S', 'Small'),
    ('L', 'Large'),
  )
  STORE_STOCK = (
    ('Out', 'not available'),
    ('In', 'availabel'),
  )
  productName = models.CharField(max_length=30, null=True)
  price = models.FloatField(max_length=30, null=True)
  sizesProduct = models.CharField(max_length=3, choices=SIZES_PRODUCT)
  storeStock = models.CharField(max_length=3, choices=STORE_STOCK)
  dateCreated = models.DateTimeField(auto_now_add=True, null=True)

class acount (models.Model):
  Customer = models.ForeignKey(customer, null=True, on_delete=models.CASCADE)
  AcountType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
  acount = models.CharField(blank=True, choices=AcountType.choices, max_length=10)

