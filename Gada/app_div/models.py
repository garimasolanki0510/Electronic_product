from django.db import models

# Create your models here.
class Product_description(models.Model):
    imagee = models.ImageField(upload_to='shop/images',default= '')
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
