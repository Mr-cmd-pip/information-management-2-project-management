from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This line includes the admin URLs
    path('courses/', include('courses.urls')),  # Include URLs from the courses app
    # Include other app URLs here
]