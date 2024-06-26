from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from examination.forms import PersonForm, NameForm
from examination.models import Person


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

