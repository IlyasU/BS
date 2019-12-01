from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from polls import views as polls_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', include('polls.urls')), #this line added
    url(r'^MainPage/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', polls_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='polls/log.html'), name='log'),
    url('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)