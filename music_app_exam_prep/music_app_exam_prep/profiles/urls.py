from django.urls import path
from music_app_exam_prep.profiles import views

urlpatterns = [
    path('details/', views.profile_details, name='profile_details'),
    path('delete/', views.profile_delete, name='profile_delete'),
]
