from django.db import models

# Create your models here.
class Product_Image (models.Model):
    image = models.ImageField(upload_to='shop/images',default= '')
    heading = models.CharField(max_length=20)