from django import forms

from .models import Groups


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = [
            'name',
            'count_students',
        ]


class GroupsCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = [
             'name',
             'count_students',
        ]


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass


