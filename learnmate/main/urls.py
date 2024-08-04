from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard, name="dashboard"),
    path('scheduler', views.scheduler, name='scheduler'),
    path('', views.dashboard, name='tasks'),
    path('assistant', views.dashboard, name='ai-assistant'),
    path('about', views.dashboard, name='about-us')
     
    
    
    
]