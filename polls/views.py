from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail
from .forms import BookingForm
from django.views.generic import View

def index(request):
    return render(request, 'polls/index.html')

def index_logged(request):
    return render(request, 'polls/index_logged.html')

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

def booking(request):
    return render(request, 'polls/book.html')

def hotels_london(request):
    return render(request, 'polls/london_hotels.html')
def info_hotel1(request):
    return render(request, 'polls/hotel1.html')
def info_hotel2(request):
    return render(request, 'polls/hotel2.html')

def hotels_newyork(request):
    return render(request, 'polls/new-york_hotels.html')
def info_hotel3(request):
    return render(request, 'polls/hotel3.html')
def info_hotel4(request):
    return render(request, 'polls/hotel4.html')

def hotels_paris(request):
    return render(request, 'polls/paris_hotels.html')
def info_hotel5(request):
    return render(request, 'polls/hotel5.html')
def info_hotel6(request):
    return render(request, 'polls/hotel6.html')

def hotels_dubai(request):
    return render(request, 'polls/dubai_hotels.html')
def info_hotel7(request):
    return render(request, 'polls/hotel7.html')
def info_hotel8(request):
    return render(request, 'polls/hotel8.html')

def hotels_moscow(request):
    return render(request, 'polls/moscow_hotels.html')
def info_hotel9(request):
    return render(request, 'polls/hotel9.html')
def info_hotel10(request):
    return render(request, 'polls/hotel10.html')

def hotels_petersburg(request):
    return render(request, 'polls/petersburg_hotels.html')
def info_hotel11(request):
    return render(request, 'polls/hotel11.html')
def info_hotel12(request):
    return render(request, 'polls/hotel12.html')

def hotels_astana(request):
    return render(request, 'polls/astana_hotels.html')
def info_hotel13(request):
    return render(request, 'polls/hotel13.html')
def info_hotel14(request):
    return render(request, 'polls/hotel14.html')

def hotels_almaty(request):
    return render(request, 'polls/almaty_hotels.html')
def info_hotel15(request):
    return render(request, 'polls/hotel15.html')
def info_hotel16(request):
    return render(request, 'polls/hotel16.html')

def reservation(request):
    return render(request, 'polls/book.html')

class BookingView(View):
    def post(self, request):
        if request.method == 'POST':
            book = BookingForm(request.POST)
            if book.is_valid():
                book.save()

        send_mail('Hello from KirIlTam(KIT)',
                  'Hello Admin! You have a new reservation, check your order on AdminPage',
                  'iitusis12@gmail.com',
                  ['dfeera1@gmail.com'],
                  fail_silently=False)
        return render(request, 'polls/congrats.html')

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





