from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('yolov8_object_tracking/', views.yolov8_object_tracking, name='yolov8_object_tracking'),    
    path('detect_object_y5/', views.detect_object_y5, name='detect_object_y5'),
    path('detect_noise/', views.detect_noise, name='detect_noise'),
    path('detect_windows/', views.detect_windows, name= 'detect_windows'),
    path('head_and_eye/', views.head_and_eye, name='head_and_eye'),
    path('yolov8_tracking/', views.yolov8_tracking, name='yolov8_tracking'),
    path('object_tracked/', views.object_tracked, name='object_tracked'),   
    path('windows_tracking/',views.windows_tracking,name='windows_tracking'), 
    path('noise_tracking/',views.noise_tracking,name='noise_tracking'),
    path('noise_plot/', views.noise_plot, name='noise_plot'),
    path('ai_proctoring/', views.ai_proctoring, name='ai_proctoring'),
    path('stop_process/', views.stop_process, name='stop_process'),
       
   
    # Add more URL patterns for other views if needed
]
