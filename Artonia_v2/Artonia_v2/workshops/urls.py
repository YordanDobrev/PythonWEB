from django.urls import path

from Artonia_v2.workshops import views

urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='workshop-list'),
    path('<int:pk>/', views.WorkshopDetailView.as_view(), name='workshop-detail'),
    path('create/', views.WorkshopCreateView.as_view(), name='workshop-create'),
]