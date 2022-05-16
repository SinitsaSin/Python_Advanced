from django import forms

from .models import Groups


class GroupsCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = [
            'name',
            'count_students',
        ]