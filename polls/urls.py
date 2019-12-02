from django.conf.urls import url
from . import views
from .views import BookingView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^User_logged', views.index_logged, name='index_logged'),
     url(r'^signUp/', views.register, name='registration'),
     url(r'^booking/', views.booking, name='booking'),

     url(r'^hotels_london/', views.hotels_london, name='hotels_london'),
     url(r'^info_hotel/', views.info_hotel1, name='info_hotel1'),
     url(r'^info_hotel2/', views.info_hotel2, name='info_hotel2'),

     url(r'^hotels_new-york/', views.hotels_newyork, name='hotels_new-york'),
     url(r'^info_hotel3/', views.info_hotel3, name='info_hotel3'),
     url(r'^info_hotel4/', views.info_hotel4, name='info_hotel4'),

     url(r'^hotels_paris/', views.hotels_paris, name='hotels_paris'),
     url(r'^info_hotel5/', views.info_hotel5, name='info_hotel5'),
     url(r'^info_hotel6/', views.info_hotel6, name='info_hotel6'),

     url(r'^hotels_dubai/', views.hotels_dubai, name='hotels_dubai'),
     url(r'^info_hotel7/', views.info_hotel7, name='info_hotel7'),
     url(r'^info_hotel8/', views.info_hotel8, name='info_hotel8'),

     url(r'^hotels_moscow/', views.hotels_moscow, name='hotels_moscow'),
     url(r'^info_hotel9/', views.info_hotel9, name='info_hotel9'),
     url(r'^info_hotel10/', views.info_hotel10, name='info_hotel10'),

     url(r'^hotels_petersburg/', views.hotels_petersburg, name='hotels_petersburg'),
     url(r'^info_hotel11/', views.info_hotel11, name='info_hotel11'),
     url(r'^info_hotel12/', views.info_hotel12, name='info_hotel12'),

     url(r'^hotels_astana/', views.hotels_astana, name='hotels_astana'),
     url(r'^info_hotel13/', views.info_hotel13, name='info_hotel13'),
     url(r'^info_hotel14/', views.info_hotel14, name='info_hotel14'),

     url(r'^hotels_almaty/', views.hotels_almaty, name='hotels_almaty'),
     url(r'^info_hotel15/', views.info_hotel15, name='info_hotel15'),
     url(r'^info_hotel16/', views.info_hotel16, name='info_hotel16'),

     url(r'^reservation/', views.reservation, name='reservation'),
     url(r'^congrats/', BookingView.as_view(), name='congrats'),

     url(r'^almaty_info/', views.city1, name='almaty'),
     url(r'^astana_info/', views.city2, name='astana'),
     url(r'^dubai_info/', views.city3, name='dubai'),
     url(r'^london_info/', views.city4, name='london'),
     url(r'^moscow_info/', views.city5, name='moscow'),
     url(r'^new-york_info/', views.city6, name='new-york'),
     url(r'^paris_info/', views.city7, name='paris'),
     url(r'^petersburg_info/', views.city8, name='petersburg'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)