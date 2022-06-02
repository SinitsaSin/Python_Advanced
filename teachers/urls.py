

from django.urls import path


from .views import get_teachers
from .views import create_teacher
from .views import update_teachers
from .views import delete_teacher

urlpatterns = [
    path('', get_teachers, name='list_teachers'),
    path('create/', create_teacher, name='create_teachers'),
    path('update/<int:pk>/', update_teachers, name='update_teachers'),
    path('delete/<int:pk>/', delete_teacher, name='delete_teachers'),
]