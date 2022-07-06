from django.urls import path
from .views import CreateGroupView
from .views import DeleteGroupView
from .views import ListGroupView
from .views import UpdateGroupView

app_name = 'groups'

urlpatterns = [
    path('create/', CreateGroupView.as_view(), name='create'),
    path('', ListGroupView.as_view(), name='list'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
]
