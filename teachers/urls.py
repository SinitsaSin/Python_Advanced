
from django.urls import path


from .views import ListTeacherView
from .views import CreateTeacherView
from .views import UpdateTeacherView
from .views import DeleteTeacherView

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list_teachers'),
    path('create/', CreateTeacherView.as_view(), name='create_teachers'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update_teachers'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete_teachers'),
]
