from django import forms
from .models import Person, TestQuestion, TestAnswer, Test, TestTheme


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
        fields = ['question', 'complexity', 'theme']

        complexity = forms.ChoiceField(choices=TestQuestion.COMPLEXITY_LEVEL, required=True)
        theme = forms.ChoiceField(choices=TestTheme.TESTS_THEMAS, required=True)


class TestAnswerForm(forms.ModelForm):
    class Meta:
        model = TestAnswer
        fields = ['answer', 'correct']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class ThemeForm(forms.Form):
    theme = forms.ModelChoiceField(queryset=TestTheme.objects.all())  # choices=TestTheme.TESTS_THEMAS queryset=TestTheme.objects.all()


class TestConfigurationForm(forms.Form):
    number_of_questions = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 91)], label='Kiek klausimų norite?')
    theme = forms.MultipleChoiceField(
        choices=[(theme.id, theme.theme) for theme in TestTheme.objects.all()],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Temos'
    )
    complexity = forms.MultipleChoiceField(
        choices=TestQuestion.COMPLEXITY_LEVEL,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Sudėtingumas'
    )
