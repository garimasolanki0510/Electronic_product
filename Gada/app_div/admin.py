from django.contrib import admin
from app_div.models import Product_description

# Register your models here.
class Pro_des(admin.ModelAdmin):
    list_display =('imagee','name','desc','price')

admin.site.register(Product_description , Pro_des)