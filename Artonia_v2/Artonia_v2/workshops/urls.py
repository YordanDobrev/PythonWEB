from django.urls import path, include

from Artonia_v2.workshops import views

urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='workshop-list'),
    path('create/', views.WorkshopCreateView.as_view(), name='workshop-create'),
    path('<int:pk>', include([
        path('', views.WorkshopDetailView.as_view(), name='workshop-detail'),
        path('delete/', views.WorkshopDeleteView.as_view(), name='workshop-delete'),
        # path('edit/', views.WorkshopEditView.as_view(), name='workshop-edit'),
    ]))
]
