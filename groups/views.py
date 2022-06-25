from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webargs.djangoparser import use_args
from .forms import GroupsCreateForm
from webargs.fields import Str, Int

from django.shortcuts import get_object_or_404
from .models import Groups

from django.views.decorators.csrf import csrf_exempt
from .utils import qshtml


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)
def get_groups(request, args):
    tc = Groups.objects.all()
    html = qshtml(tc)
    # return HttpResponse(html)
    return render(
        request,
        'groups/list.html',
        {'title': 'List of groups', 'groups': tc}

    )


@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupsCreateForm()
    else:
        form = GroupsCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_groups'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_groups(request, pk):
    group = Groups.objects.get(pk=pk)
    if request.method == 'POST':
        form = GroupsCreateForm(instance=group)
    else:
        form = GroupsCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_groups'))

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list_groups'))

    return render(request, 'groups/delete.html', {'teacher': group})
