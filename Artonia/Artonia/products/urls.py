from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dash'),
    path('add-macrame/', views.add_macrame, name='add-macrame'),
    path('add-art-painting/', views.add_art_painting, name='add-art-painting'),
]