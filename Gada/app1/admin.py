from django.contrib import admin

# Register your models here.

from app1.models import Product_Image

# Register your models 

class Pro_Img(admin.ModelAdmin):
    list_display = ('image', 'heading' )

admin.site.register(Product_Image , Pro_Img)