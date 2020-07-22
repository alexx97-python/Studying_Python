from django.urls import path
from .views import index, update_task, delete_task

app_name = 'tasks'

urlpatterns = [
    path('home/', index, name='home'),
    path('update_task/<str:pk>', update_task, name='update_task'),
    path('delete_task/<str:pk>', delete_task, name='delete_task'),
]