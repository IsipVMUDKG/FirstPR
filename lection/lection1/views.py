from django.shortcuts import render
from django.http import HttpResponse

def index(requets):
    return HttpResponse('Йоу ЛЕКЦИИИИИЯЯЯЯЯ')

def Index(requets):
    return render(requets, 'Index.html')

def About(requets):
    return render(requets, 'About.html')

def Contacts(requets):
    return render(requets, 'Contacts.html')

def Location(requets):
    return render(requets, 'Location.html')

def Tariffs(requets):
    return render(requets, 'Tariffs.html')