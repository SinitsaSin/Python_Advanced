from django.urls import path
from .views import get_students
from .views import create_students
from .views import delete_student
from .views import update_students

urlpatterns = [
    path('', get_students, name='list_students'),
    path('create/', create_students, name='create_students'),
    path('update/<int:pk>/', update_students, name='update_students'),
    path('delete/<int:pk>/', delete_student, name='delete_students'),
]
