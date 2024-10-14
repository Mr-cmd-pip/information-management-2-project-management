from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('profile/delete/confirm/', views.confirm_delete_profile, name='confirm_delete_profile'),
    path('profile/delete/confirm/cancel/', views.cancel_delete_profile, name='cancel_delete_profile'),
]
