from django.shortcuts import render
from django.http import HttpResponse
from .models import Teachers
from .utils import qshtml

def get_teachers(request):
    tc = Teachers.objects.all()
    html = qshtml(tc)
    return HttpResponse(html)

