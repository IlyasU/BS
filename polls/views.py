from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Countries, Choice

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import UserRegisterForm


def index(request):
    return render(request, 'polls/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}!')
            return render(request, 'polls/signUp.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'polls/signUp.html', {'form': form})


def city1(request):
    return render(request, 'polls/almaty_hotels.html')

def city2(request):
    return render(request, 'polls/astana_hotels.html')

def city3(request):
    return render(request, 'polls/dubai_hotels.html')

def city4(request):
    return render(request, 'polls/london_hotels.html')

def city5(request):
    return render(request, 'polls/moscow_hotels.html')

def city6(request):
    return render(request, 'polls/new-york_hotels.html')

def city7(request):
    return render(request, 'polls/paris_hotels.html')

def city8(request):
    return render(request, 'polls/petersburg_hotels.html')

