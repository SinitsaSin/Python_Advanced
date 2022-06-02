
from django.contrib import admin
from core.views import index
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
]
