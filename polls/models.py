from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Countries(models.Model):
   country_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.country_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    Country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Booking(models.Model):
    name = models.CharField('Имя', max_length=120)
    lastname = models.CharField('Фамилия', max_length=120)
    email = models.EmailField('Почта', max_length=120, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=120)
    address = models.CharField('Домашний Адрес', max_length=120)



    def __str__(self):
        return self.name



