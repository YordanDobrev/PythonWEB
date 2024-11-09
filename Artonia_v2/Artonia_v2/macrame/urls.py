from django.urls import path

from Artonia_v2.macrame import views

urlpatterns = [
    path('create/', views.CreateMacrameView.as_view(), name='create_macrame'),
]