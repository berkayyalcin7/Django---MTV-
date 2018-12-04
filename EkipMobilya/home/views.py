# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response,render,HttpResponse
from django.core.context_processors import csrf

from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")