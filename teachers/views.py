from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .forms import TeachersCreateForm, TeacherFilterForm
from .models import Teachers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class ListTeacherView(ListView):
    model = Teachers
    template_name = 'teachers/list.html'


class CreateTeacherView(CreateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('list_teachers')
    template_name = 'teachers/update.html'


class UpdateTeacherView(UpdateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('list_teachers')
    template_name = 'teachers/update.html'


class DeleteTeacherView(DeleteView):
    model = Teachers
    success_url = reverse_lazy('list_teachers')
    template_name = 'teachers/delete.html'


