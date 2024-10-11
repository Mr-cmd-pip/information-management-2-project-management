from django.urls import path
from .views import create_course, course_list, course_detail, edit_course, delete_course

urlpatterns = [
    path('create/', create_course, name='create_course'),  # URL for creating a course
    path('', course_list, name='course_list'),  # URL for listing courses
    path('<int:course_id>/', course_detail, name='course_detail'),  # URL for course detail
    path('<int:course_id>/edit/', edit_course, name='edit_course'),  # URL for editing a course
    path('<int:course_id>/delete/', delete_course, name='delete_course'),  # URL for deleting a course
]
