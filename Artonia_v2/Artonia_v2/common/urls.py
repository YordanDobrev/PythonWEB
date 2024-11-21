from django.urls import path

from Artonia_v2.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
]
