from django import forms
from .models import Stock




from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class StockForm(forms.ModelForm):
    class Meta: 
        model = Stock
        fields = ["ticker"]

