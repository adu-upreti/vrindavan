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

 

class Add_Team(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='team/image')
    designation = models.CharField(max_length=1000)

class RestaurantInfo(models.Model):
    description1 = models.TextField("Paragraph 1")
    description2 = models.TextField("Paragraph 2")

    def __str__(self):
        return "Restaurant Information"
