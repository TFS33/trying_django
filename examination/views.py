from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from examination.forms import PersonForm, NameForm, TestQuestionForm, TestAnswerForm, TestForm, TestConfigurationForm
from examination.models import Person, Test, TestQuestion, TestAnswer, TestTheme
from .helpers.test_config import get_all_questions, populate_answer_fields


def index(request):
    return HttpResponse("Hello, world. You're at the examination index.")


def persons(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'examination/persons.html', context)


def person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {'person': person, 'pk': pk}
    return render(request, 'examination/person.html', context)


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('examination:persons')


def person_delete_2(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {'person': person, 'pk': pk}
    if request.method == 'POST':
        person.delete()
        return redirect('examination:persons')
    return render(request, 'examination/person_delete.html', context)


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('examination:persons')
    else:
        form = PersonForm(instance=person)
    return render(request, 'examination/person_update.html', {'form': form, 'person': person})


def person_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('examination:persons')
    else:
        form = PersonForm()
    return render(request, 'examination/person_add.html', {'form': form})


def add_person_2(request):
    context = {'person': 1}
    if request.method == 'POST':
        data = request.POST
        person = Person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=data['birth_date'],
        )
        person.save()
        return redirect('examination:persons')
    return render(request, 'examination/person_add_2.html', context)


def add_person_3(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person(
                first_name=data['your_name'],
                last_name=data['your_last_name'],
                birth_date=data['your_birth_day'],
            )
            person.save()
            return redirect('examination:persons')
        else:
            return render(request, 'examination/person_add_3.html', {'form': form})
    else:
        form = NameForm()
        return render(request, 'examination/person_add_3.html', {'form': form})


def show_questions(request):
    questions = TestQuestion.objects.all()
    context = {'questions': questions}
    return render(request, 'examination/questions.html', context)


def add_question(request):
    if request.method == 'POST':
        form = TestQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('examination:show_questions')
    else:
        form = TestQuestionForm()

    return render(request, 'examination/add_question.html', {'form': form})


def delete_question(request, pk):
    question = get_object_or_404(TestQuestion, pk=pk)
    question.delete()
    return redirect('examination:add_question')


# def add_answer(request, pk):
#     question = get_object_or_404(TestQuestion, pk=pk)
#     answers = TestAnswer.objects.filter(question=question)
#     if request.method == 'POST':
#         form = TestAnswerForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             answer = TestAnswer(
#                 answer=data['answer'],
#                 question=data['question'],
#                 correct=data['correct'],
#             )
#             answer.save()
#             return redirect('examination:add_answer', pk=pk)
#     else:
#         form = TestAnswerForm()
#
#     context = {
#         'answers': answers,
#         'form': form,
#         'pk': pk,
#         'question': question
#     }
#     return render(request, 'examination/answers.html', context)

def add_answer(request, pk):
    question = get_object_or_404(TestQuestion, pk=pk)

    answers = TestAnswer.objects.filter(question=question)

    if request.method == 'POST':
        form = TestAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('examination:add_answer', pk=pk)
    else:
        form = TestAnswerForm()

    context = {
        'question': question,
        'answers': answers,
        'form': form
    }
    return render(request, 'examination/answers.html', context)


def delete_answer(request, pk_question, pk_answer):
    answer = get_object_or_404(TestAnswer, pk=pk_answer)
    answer.delete()
    return redirect('examination:add_answer', pk=pk_question)


def update_question(request, pk):
    question = get_object_or_404(TestQuestion, pk=pk)
    if request.method == 'POST':
        form = TestQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('examination:add_answer', pk=question.pk)
    else:
        form = TestQuestionForm(instance=question)

    return render(request, 'examination/update_question.html', {'form': form, 'question': question})


def question(request):
    return render(request, 'examination/question.html')


def show_tests(request, ):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'examination/configure_test.html', context)


def configure_test(request):
    if request.method == 'POST':
        form = TestConfigurationForm(request.POST)
        if form.is_valid():
            num_questions = int(form.cleaned_data['number_of_questions'])
            themes = form.cleaned_data['theme']
            complexities = form.cleaned_data['complexity']

            questions = TestQuestion.objects.all()
            if themes:
                questions = questions.filter(theme__in=themes)
            if complexities:
                questions = questions.filter(complexity__in=[int(c) for c in complexities])

            questions = list(questions.order_by('?')[:num_questions])

            questions_with_answers = [(question, populate_answer_fields(question)) for question in questions]

            return render(request, 'examination/show_test.html', {'questions_with_answers': questions_with_answers})

    else:
        form = TestConfigurationForm()

    return render(request, 'examination/configure_test.html', {'form': form})


