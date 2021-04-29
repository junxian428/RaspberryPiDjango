
from django.conf.urls import url

from led import views

urlpatterns = [
    url(r'led/turnOn', views.turnOn, name='turnOn'),
    url(r'led/turnOff', views.turnOff, name='turnOff'),
]



