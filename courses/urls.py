from django.urls import path

from .views import create_course
from .views import delete_course
from .views import get_courses
from .views import update_courses


urlpatterns = [
    path('create/', create_course, name='create_courses'),
    path('', get_courses, name='list_courses'),
    path('update/<int:pk>/', update_courses, name='update_courses'),
    path('delete/<int:pk>/', delete_course, name='delete_courses'),
]