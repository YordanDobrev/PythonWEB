from django.urls import path
from tasty_recypes.profiles import views

urlpatterns = [
    path('details/', views.profile_details, name='profile_details'),
    path('create/', views.profile_create, name='profile_create'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.profile_delete, name='profile_delete'),
]
