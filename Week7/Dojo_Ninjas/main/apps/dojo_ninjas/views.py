# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Placeholder for Dojo Ninjas')


# Create your views here.