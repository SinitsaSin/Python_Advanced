from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import GroupsCreateForm
from .models import Groups
from .utils import qshtml
from webargs.fields import Str, Int
from webargs.djangoparser import use_args
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse('LMS System!')

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
    #return HttpResponse(html)
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

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type = "submit" value="Create">
            <form>
        """

    return HttpResponse(html_form)

@csrf_exempt
def update_groups(request, pk):
    group = Groups.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupsCreateForm(instance=group)
    else:
        form = GroupsCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list_groups'))

    html_form = f"""
            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type = "submit" value="Update">
            <form>
        """

    return HttpResponse(html_form)

def delete_group(request ,pk):
    group = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list_groups'))

    return render(request, 'groups/delete.html', {'teacher': group})




