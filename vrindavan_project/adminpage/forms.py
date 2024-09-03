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

class AddteamForm(forms.ModelForm):
    class Meta:
        model = Add_Team
        fields = '__all__'

class RestaurantInfoForm(forms.ModelForm):
    class Meta:
        model = RestaurantInfo
        fields = ['description1', 'description2']
        widgets = {
            'description1': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'description2': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }



 

