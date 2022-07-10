from django.contrib import admin
from teachers.models import Teachers


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'group',
    ]

    list_display_links = list_display
    search_fields = [
        'first_name',
        'last_name',
    ]
    list_filter = [
        'group',
    ]

    fields = [
        ('first_name', 'last_name'),
        ('age',),
        'phone_number',
        'group',
    ]


admin.site.register(Teachers, TeacherAdmin)
