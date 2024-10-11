from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm  # Import the CourseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View to create a new course
@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user  # Set the logged-in user as the course owner
            course.save()
            messages.success(request, 'Course created successfully!')
            return redirect('course_detail', course_id=course.id)  # Redirect to the detail view
        else:
            messages.error(request, 'Error creating the course. Please check the form.')
    else:
        form = CourseForm()
    
    return render(request, 'courses/create_course.html', {'form': form})

# View to list all courses
@login_required
def course_list(request):
    courses = Course.objects.all()  # Retrieve all courses
    return render(request, 'courses/course_list.html', {'courses': courses})

# View to show the details of a single course
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

# View to allow users to edit a course (assuming only the owner can edit)
@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if course.owner != request.user:
        messages.error(request, 'You are not authorized to edit this course.')
        return redirect('course_detail', course_id=course_id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('course_detail', course_id=course_id)
        else:
            messages.error(request, 'Error updating the course. Please check the form.')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

# View to allow users to delete a course (only the owner can delete)
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if course.owner != request.user:
        messages.error(request, 'You are not authorized to delete this course.')
        return redirect('course_detail', course_id=course_id)
    
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully!')
        return redirect('course_list')
    
    return render(request, 'courses/delete_course.html', {'course': course})
