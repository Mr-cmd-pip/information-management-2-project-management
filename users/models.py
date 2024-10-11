from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  # Custom role for admins

    # Override the groups field to prevent conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )

    # Override the user_permissions field to prevent conflicts
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    # Custom method to check user roles
    def is_instructor(self):
        return self.is_teacher

    def is_student_user(self):
        return self.is_student
