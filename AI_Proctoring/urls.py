from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_proctoring.urls')),  # Include your app's URLs
    # Add more project-wide URL patterns if needed
]
