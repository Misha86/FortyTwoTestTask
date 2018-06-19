from django.shortcuts import render
from apps.hello.models import Person

# Create your views here.


def contacts(request):
    person = Person.objects.get(name="Misha")
    return render(request, 'contacts.html', {'person': person})
