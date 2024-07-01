from django import forms
from .models import Person, TestQuestion, TestAnswer


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date']


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
    your_last_name = forms.CharField(max_length=100)
    your_birth_day = forms.DateField()


class TestQuestionForm(forms.ModelForm):
    class Meta:
        model = TestQuestion
        fields = "__all__"


class TestAnswerForm(forms.ModelForm):
    class Meta:
        model = TestAnswer
        fields = ['answer', 'correct']
