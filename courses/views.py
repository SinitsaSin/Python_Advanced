from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webargs.djangoparser import use_args
from .forms import CoursesCreateForm
from webargs.fields import Str, Int

from django.shortcuts import get_object_or_404
from .models import Courses

from django.views.decorators.csrf import csrf_exempt
from .utils import qshtml


@use_args(
    {
        'name': Str(required=False),
        'count_students': Int(required=False)
    },
    location='query'
)
def get_courses(request, args):
    tc = Courses.objects.all()
    html = qshtml(tc)
    return render(
        request,
        'courses/list.html',
        {'title': 'List of courses', 'courses': tc}

    )


@csrf_exempt
def create_course(request):
    if request.method == 'GET':
        form = CoursesCreateForm()
    else:
        form = CoursesCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_courses'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_courses(request, pk):
    course = Courses.objects.get(pk=pk)
    if request.method == 'GET':
        form = CoursesCreateForm(instance=course)
    else:
        form = CoursesCreateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_courses'))

    return render(
        request=request,
        template_name='courses/update.html',
        context={'form': form}
    )


def delete_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('list_courses'))

    return render(request, 'courses/delete.html', {'course': course})
