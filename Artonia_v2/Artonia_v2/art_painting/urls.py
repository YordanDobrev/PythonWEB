from django.urls import path

from Artonia_v2.art_painting import views

urlpatterns = [
    path('create/', views.CreateArtPaintingView.as_view(), name='create-art-painting'),
]