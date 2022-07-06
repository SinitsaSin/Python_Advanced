from core.views import index
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
