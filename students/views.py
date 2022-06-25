from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentsCreateForm
from .models import Students
from django.shortcuts import get_object_or_404
from .forms import StudentFilterForm

def get_students(request):
    students = Students.objects.all()
    students_filter = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request,
        'students/list.html',
        {'students_filter': students_filter}
    )


@csrf_exempt
def create_students(request):
    if request.method == 'GET':
        form = StudentsCreateForm()
    else:
        form = StudentsCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_students'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_students(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == 'GET':
        form = StudentsCreateForm(instance=student)
    else:
        form = StudentsCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_students'))

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )


def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('list_students'))

    return render(request, 'students/delete.html', {'teacher': student})



