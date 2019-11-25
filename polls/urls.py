from django.conf.urls import url, include
from polls.views import MyRegisterFormView
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^registration/$', views.register, name='register'),
     url(r'^signUp.html/$', views.register, name='registration'),
     url(r'^almaty_hotels.html', views.city1, name='almaty'),
     url(r'^astana_hotels.html', views.city2, name='astana'),
     url(r'^dubai_hotels.html', views.city3, name='dubai'),
     url(r'^london_hotels.html', views.city4, name='london'),
     url(r'^moscow_hotels.html', views.city5, name='moscow'),
     url(r'^new-york_hotels.html', views.city6, name='new-york'),
     url(r'^paris_hotels.html', views.city7, name='paris'),
     url(r'^petersburg_hotels.html', views.city8, name='petersburg'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)