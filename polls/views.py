from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Countries, Choice

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from django.contrib import auth

def index(request):
    return render(request, 'polls/index.html')

def index_logged(request):
    return render(request, 'polls/index_logged.html')

def log(request):
    return render(request, 'polls/log.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}!')
            return render(request, 'polls/index.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'polls/signUp.html', {'form': form})


def city1(request):
    return render(request, 'polls/almaty_info.html')

def city2(request):
    return render(request, 'polls/astana_info.html')

def city3(request):
    return render(request, 'polls/dubai_info.html')

def city4(request):
    return render(request, 'polls/london_info.html')

def city5(request):
    return render(request, 'polls/moscow_info.html')

def city6(request):
    return render(request, 'polls/new-york_info.html')

def city7(request):
    return render(request, 'polls/paris_info.html')

def city8(request):
    return render(request, 'polls/petersburg_info.html')

