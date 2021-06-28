from .models import Product
from django import forms
from .widgets import CustomClearableFileInput



class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        exclude = ('favourites',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
