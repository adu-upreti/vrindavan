from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'



 

