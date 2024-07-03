from django.db.models import QuerySet
from examination.models import TestQuestion, TestAnswer
import random


def get_all_questions() -> QuerySet[TestQuestion]:
    return TestQuestion.objects.all()


def populate_answer_fields(question: TestQuestion):
    all_answers = list(question.testanswer_set.all())
    correct_answers = [answer for answer in all_answers if answer.correct]
    incorrect_answers = [answer for answer in all_answers if not answer.correct]

    if len(correct_answers) >= 1 and len(incorrect_answers) >= 3:
        correct_answer = random.choice(correct_answers)
        incorrect_answers = random.sample(incorrect_answers, 3)

        answers_for_question = incorrect_answers + [correct_answer]
        random.shuffle(answers_for_question)
        return answers_for_question

    else:
        raise Exception('Not enough answers')
