from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Make sure this line is present
    path('', include('courses.urls')),       # Include other app URLs
]
