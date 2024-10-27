from django.urls import path

from RegularExam.author import views

urlpatterns = [
    path('create/', views.author_creation, name='author_create'),
    path('edit/', views.author_edit, name='author_edit'),
    path('delete/', views.author_delete, name='author_delete'),
    path('details/', views.author_details, name='author_details'),
]
