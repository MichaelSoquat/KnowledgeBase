from django import forms

from knowledge.add.models import Knowledge

class AddForm(forms.Form):
    class Meta:
        model = Knowledge
        fields = ['title','text','autor']