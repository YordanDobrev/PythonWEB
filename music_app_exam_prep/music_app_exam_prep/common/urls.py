from django.urls import path
from music_app_exam_prep.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
]