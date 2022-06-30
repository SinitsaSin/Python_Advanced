from django import forms

from .models import Courses


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'name',
            'count_students',
        ]


class CoursesCreateForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'name',
            'count_students',
        ]


class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass
