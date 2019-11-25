from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Countries, Choice

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'polls/index.html')


def register(request):
    return render(request, 'polls/signUp.html')

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


# Вариант регистрации на базе класса FormView
class MyRegisterFormView(FormView):
        # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
        # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

        # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
        # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "polls/index.html/"

        # Шаблон, который будет использоваться при отображении представления.
    template_name = "polls/signUp.html"

    def form_valid(self, form):
        form.save()
            # Функция super( тип [ , объект или тип ] )
            # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView(), self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView(), self).form_invalid(form)