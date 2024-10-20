from django.urls import path, include

from ExamPrepOne.account import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('profile/', include([
        path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('delete/', views.DeleteProfileView.as_view(), name='profile-delete'),
    ])),
]
