from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('scheduler', views.scheduler, name='scheduler'),
    path('tasks', views.tasks, name='tasks'),
    path('assistant', views.dashboard, name='ai-assistant'),
    path('about', views.dashboard, name='about-us'),
    path('delete/<int:item_id>/', views.delete_todo_item, name='delete_todo_item'), 
    
]