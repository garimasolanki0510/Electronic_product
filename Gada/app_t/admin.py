from django.contrib import admin
from app_t.models import Product_table


# Register your models here.
class Pro_table(admin.ModelAdmin):
    list_display = ('pro_name' ,'pro_con' ,'pro_rel' ,'pro_price' ,'pro_avail')

admin.site.register(Product_table,Pro_table)