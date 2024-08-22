from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
   cat_name = models.CharField(max_length=200)

   def __str__(self):
        return self.cat_name

class Products(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='product/image')
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="products")

    def __str__(self):
     return self.name

