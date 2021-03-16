from django import forms

class InvestmentsByCity(forms.Form):
    entry = forms.CharField(max_length= 256)

class InvestmentsByCityProgress(forms.Form):
    entry = forms.CharField(max_length= 256)
    entry2 = forms.CharField(max_length= 256)