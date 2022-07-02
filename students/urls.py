from django.urls import path
from .views import ListStudentView
from .views import CreateStudentView
from .views import DeleteStudentView
from .views import UpdateStudentView

urlpatterns = [
    path('', ListStudentView.as_view(), name='list_students'),
    path('create/', CreateStudentView.as_view(), name='create_students'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update_students'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete_students'),
]
