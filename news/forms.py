from django import forms
from .models import News,Category



class AddNews(forms.ModelForm):
    class Meta:
        model=News
        fields="__all__"




class AddCategory(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"








