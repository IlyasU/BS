from django.conf.urls import url, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^User_logged', views.index_logged, name='index_logged'),
     url(r'^signUp/', views.register, name='registration'),
     url(r'^login/', views.log, name='log'),
     url(r'^almaty_info/', views.city1, name='almaty'),
     url(r'^astana_info/', views.city2, name='astana'),
     url(r'^dubai_info/', views.city3, name='dubai'),
     url(r'^london_info/', views.city4, name='london'),
     url(r'^moscow_info/', views.city5, name='moscow'),
     url(r'^new-york_info/', views.city6, name='new-york'),
     url(r'^paris_info/', views.city7, name='paris'),
     url(r'^petersburg_info/', views.city8, name='petersburg'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)