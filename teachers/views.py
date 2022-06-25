from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import TeachersCreateForm, TeacherFilterForm
from .models import Teachers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


def get_teachers(request):
    teachers = Teachers.objects.all()
    teachers_filter = TeacherFilterForm(data=request.GET, queryset=teachers)

    return render(
        request,
        'teachers/list.html',
        {'teachers_filter': teachers_filter}

    )


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeachersCreateForm()
    else:
        form = TeachersCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_teachers'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_teachers(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == 'GET':
        form = TeachersCreateForm(instance=teacher)
    else:
        form = TeachersCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_teachers'))

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('list_teachers'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})
