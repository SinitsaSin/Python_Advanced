from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import GroupsCreateForm
from .models import Groups


class ListGroupView(LoginRequiredMixin, ListView):
    model = Groups
    template_name = 'groups/list.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Groups
    form_class = GroupsCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    model = Groups
    form_class = GroupsCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Groups
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
