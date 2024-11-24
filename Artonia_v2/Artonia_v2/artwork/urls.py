from django.urls import path, include

from Artonia_v2.artwork import views

urlpatterns = [
    path('', views.PublicArtworkListView.as_view(), name='public_artwork_list'),
    # path('<slug:slug>/', include([
    #     path('', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    #     path('like/', views.toggle_artwork_like, name='artwork_like'),
    #     path('share/', views.share_artwork, name='artwork_share'),
    # ])),
]
