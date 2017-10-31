from django import forms

class AddForms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
