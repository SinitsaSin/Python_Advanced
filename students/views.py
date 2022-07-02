from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from core.views import UpdateBaseView
from .forms import StudentsCreateForm
from .models import Students
from django.shortcuts import get_object_or_404


class ListStudentView(ListView):
    model = Students
    template_name = 'students/list.html'


class CreateStudentView(CreateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('list_students')
    template_name = 'students/update.html'


class UpdateStudentView(UpdateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('list_students')
    template_name = 'students/update.html'


class DeleteStudentView(DeleteView):
    model = Students
    success_url = reverse_lazy('list_students')
    template_name = 'students/delete.html'

