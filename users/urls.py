from django.urls import path
from .views import login_view, logout_view, signup_view  # Import the signup_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Login URL
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('signup/', signup_view, name='signup'),  # Signup URL
]
