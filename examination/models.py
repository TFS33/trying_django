from django.db import models

from django.utils import timezone


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


TESTS_THEMAS = [
    ("Animals", "Gyvunai"),
    ("KET", "Kelių eismo taisyklės"),
    ("Flowers", "Gėlės"),
]


class Test(BaseModel):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=50, choices=TESTS_THEMAS)

    def __str__(self):
        return f'{self.subject} {self.topic}'


class TestQuestion(BaseModel):
    COMPLEXITY_LEVEL = {
        '1': "Easy",
        '2': "Medium",
        '3': "Hard",
    }
    question = models.CharField(max_length=100)
    complexity = models.CharField(max_length=50, choices=COMPLEXITY_LEVEL)

    def __str__(self):
        return f'{self.question} {self.complexity}'


class TestAnswer(BaseModel):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} {self.answer} {self.correct}'


class ExaminationQuestion(BaseModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test} {self.question}'


class TestResult(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person} {self.test}'

# Create your models here.
