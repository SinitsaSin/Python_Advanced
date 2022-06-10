from django.urls import path

from .views import create_group
from .views import delete_group
from .views import get_groups
from .views import update_groups


urlpatterns = [
    path('create/', create_group, name='create_groups'),
    path('', get_groups, name='list_groups'),
    path('update/<int:pk>/', update_groups, name='update_groups'),
    path('delete/<int:pk>/', delete_group, name='delete_groups'),
]
