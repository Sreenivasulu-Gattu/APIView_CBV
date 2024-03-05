from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['id','pro_cat_id','pro_id','pro_name','pro_price']

admin.site.register(ProductCatagory)

admin.site.register(Product,cust)