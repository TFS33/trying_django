from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

from examination.models import Person


def home(request):
    return render(request, 'home/home.html')

