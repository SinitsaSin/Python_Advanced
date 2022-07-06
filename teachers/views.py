from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .forms import TeachersCreateForm, TeacherFilterForm
from .models import Teachers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class ListTeacherView(LoginRequiredMixin, ListView):
    model = Teachers
    template_name = 'teachers/list.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teachers
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'


