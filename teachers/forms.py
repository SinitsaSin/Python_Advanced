from django import forms
from django_filters import FilterSet

from .models import Teachers


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = [
            'first_name',
            'last_name',
            'age',
            'phone_number',
        ]

    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['last_name']
        return ln.title()

    def clean_phone_number(self):
        pn = self.cleaned_data['phone_number']
        lst = []
        for element in pn:
            if element in '0123456789':
                lst.append(element)
        return ''.join(lst)


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teachers
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
