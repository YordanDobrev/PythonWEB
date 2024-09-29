from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add_page, name='add-photo'),
    path('<int:pk>', views.photo_details_page, name='photo-details'),
    path('<int:pk>/edit', views.photo_edit_page, name='photo-edit'),
]
