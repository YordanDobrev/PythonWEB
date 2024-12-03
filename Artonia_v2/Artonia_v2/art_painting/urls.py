from django.urls import path, include

from Artonia_v2.art_painting import views

urlpatterns = [
    path('create/', views.CreateArtPaintingView.as_view(), name='create-art-painting'),
    path('<int:pk>/', include([
        path('edit/', views.UpdateArtPaintingView.as_view(), name='edit_art-painting'),
        path('details/', views.ArtPaintingDetailsView.as_view(), name='details_art-painting'),
        path('delete/', views.ArtPaintingDeleteView.as_view(), name='delete_art-painting'),
        path('like/', views.LikeToggleView.as_view(), name='art_like_toggle'),
    ]))]
