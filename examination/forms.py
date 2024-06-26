from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date']


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
    your_last_name = forms.CharField(max_length=100)
    your_birth_day = forms.DateField()
