from django.urls import path

from ExamPrep_WOS.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]