from django.db import models

# Create your models here.


class ProductCatagory(models.Model):
    pro_cat_id = models.PositiveIntegerField(primary_key = True)
    pro_cat_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.pro_cat_name

class Product(models.Model):
    pro_cat_id = models.ForeignKey(ProductCatagory,on_delete = models.CASCADE)
    pro_id  = models.PositiveIntegerField()
    pro_name = models.CharField(max_length = 100)
    pro_price = models.PositiveIntegerField()

