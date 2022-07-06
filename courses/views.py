from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CoursesCreateForm
from .models import Courses


class ListCourseView(LoginRequiredMixin, ListView):
    model = Courses
    template_name = 'courses/list.html'


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Courses
    form_class = CoursesCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Courses
    form_class = CoursesCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Courses
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
