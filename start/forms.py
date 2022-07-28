from django.forms import forms

class Input(forms.Form):
    field = forms.CharField(max_length=20, widget=forms.Select(attrs={'onchange': 'submit();'}))