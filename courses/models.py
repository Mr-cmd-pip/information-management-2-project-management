from django.db import models
from users.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=7, default="#FFFFFF")  # For color-coding
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses')  # Teacher of the course
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add a field for students enrolled in the course
    students = models.ManyToManyField(CustomUser, related_name='enrolled_courses', blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Optional: Add a field for attached files
    attached_file = models.FileField(upload_to='course_files/', blank=True, null=True)

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'
