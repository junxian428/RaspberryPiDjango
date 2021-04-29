# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import RPi.GPIO as GPIO
from django.http import HttpResponse


LED_PIN = 32

def turnOn(request): 
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(32,GPIO.OUT)
   GPIO.output(LED_PIN, 1)
   return HttpResponse('')


def turnOff(request):
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(32,GPIO.OUT)
   GPIO.output(LED_PIN, 0)
   return HttpResponse('')

