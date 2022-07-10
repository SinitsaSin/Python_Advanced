from django.contrib import admin  # noqa
from groups.models import Groups
from students.models import Students
from teachers.models import Teachers


class StudentsInlineTable(admin.TabularInline):
    model = Students
    fields = [
        'first_name',
        'last_name',
        'age',
        'phone_number',
    ]


class TeachersInlineTable(admin.TabularInline):
    model = Teachers
    fields = [
        'first_name',
        'last_name',
        'age',
        'phone_number',
    ]


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'count_students',
        'main_course',
    ]

    fields = [
        'name',
        'count_students',
        'main_course',
    ]

    inlines = [TeachersInlineTable, StudentsInlineTable]


admin.site.register(Groups, GroupAdmin)
