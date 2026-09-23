from django.contrib import admin
from django.urls import path, include
from tasks.views import home, register, add_task, edit_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('task/add/', add_task, name='add_task'),
    path('task/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
]