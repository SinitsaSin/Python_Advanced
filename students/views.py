from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentsCreateForm
from .models import Students
from .utils import qshtml
from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args

@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)
def get_students(request, args):
    st = Students.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})

    html = qshtml(st)
    return HttpResponse (html)

@csrf_exempt
def create_students(request):
    if request.method == 'GET':
        form = StudentsCreateForm()
    else:
        form = StudentsCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/get_students/')

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type = "submit" value="Submit">
            <form>
        """

    return HttpResponse(html_form +'CREATE')

