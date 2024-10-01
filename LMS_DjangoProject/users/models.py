from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  # Custom role for admins

    # Custom method to check user roles
    def is_instructor(self):
        return self.is_teacher

    def is_student(self):
        return self.is_student
