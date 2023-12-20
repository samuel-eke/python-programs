from django import forms
from .models import Proudcts

class CreateProductform(forms.ModelForm):
    class Meta:
        model = Proudcts
        fields = [
            'title', 'description', 'price'
        ]