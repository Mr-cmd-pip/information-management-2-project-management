from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm  # Import the CourseForm
from django.contrib.auth.decorators import login_required

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user  # Set the logged-in user as the course owner
            course.save()
            return redirect('course_detail', course_id=course.id)  # Redirect to the detail view
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def course_list(request):
    courses = Course.objects.all()  # Retrieve all courses
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})


