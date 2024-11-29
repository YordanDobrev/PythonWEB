from django.urls import path, include

from Artonia_v2.artwork import views

urlpatterns = [
    path('', views.PublicArtworkListView.as_view(), name='public_artwork_list'),
]
