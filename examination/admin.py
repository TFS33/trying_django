from django.contrib import admin

from .models import Person, Test, TestQuestion, TestAnswer, ExaminationQuestion, TestResult, TestTheme

class ChoiceInline(admin.TabularInline):
    model = TestAnswer
    extra = 4


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'complexity', 'test_theme')


admin.site.register(Person)
admin.site.register(Test)
admin.site.register(TestQuestion, QuestionsAdmin)
admin.site.register(ExaminationQuestion)
admin.site.register(TestResult)
admin.site.register(TestTheme)

# Register your models here.
