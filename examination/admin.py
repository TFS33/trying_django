from django.contrib import admin


from .models import Person, Test, TestQuestion, TestAnswer, ExaminationQuestion, TestResult

class ChoiceInline(admin.TabularInline):
    model = TestAnswer
    extra = 4


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Person)
admin.site.register(Test)
admin.site.register(TestQuestion, QuestionsAdmin)
admin.site.register(ExaminationQuestion)
admin.site.register(TestResult)

# Register your models here.
