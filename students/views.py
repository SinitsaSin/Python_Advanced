from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from .forms import StudentsCreateForm
from .models import Students


class ListStudentView(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'students/list.html'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
