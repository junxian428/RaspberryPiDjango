from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.turnOn, name='turnOn'),
    url(r'^$', views.turnOff, name='turnOff'),
]
