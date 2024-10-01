from django.db import models

# Create your models here.
class Product_table(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_con = models.CharField(max_length=20)
    pro_rel = models.CharField(max_length=20)
    pro_price = models.CharField(max_length=20)
    pro_avail = models.CharField(max_length=20)
    