from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import TeachersCreateForm
from .models import Teachers
from .utils import qshtml
from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('LMS System!')



@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)

def get_teachers(request, args):
    tc = Teachers.objects.all()
    html = qshtml(tc)
    return HttpResponse(html)

@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeachersCreateForm()
    else:
        form = TeachersCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/get_teachers/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type = "submit" value="Submit">
            <form>
        """

    return HttpResponse(html_form +'CREATE')

