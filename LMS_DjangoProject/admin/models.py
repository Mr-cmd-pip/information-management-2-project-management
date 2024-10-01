from django.db import models
from users.models import CustomUser

class AdminSettings(models.Model):
    admin_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    max_course_limit = models.IntegerField(default=10)  # Example of system-wide settings
    # Add other system-wide settings