from django.db import models


# Create your models here.
# models == tables

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # DecimalField special for price type
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) # CASCADE and PROTECT and SET_DEFAULT
