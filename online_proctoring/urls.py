from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('detect_object_y5/', views.detect_object_y5, name='detect_object_y5'),
    path('detect_noise/', views.detect_noise, name='detect_noise'),
    path('head_and_eye/', views.head_and_eye, name='head_and_eye'),
    path('object_tracked/', views.object_tracked, name='object_tracked'),   
    path('noise_tracking/',views.noise_tracking,name='noise_tracking'),
    path('noise_plot/', views.noise_plot, name='noise_plot'),
    path('ai_proctoring/', views.ai_proctoring, name='ai_proctoring'),
    path('stop_process/', views.stop_process, name='stop_process'),
    path('head_nose_tracked/',views.head_nose_tracked, name='head_nose_tracked'),
]
