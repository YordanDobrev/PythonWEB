from django.urls import path, include

from ExamPrepOne.album import views

urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('<int:pk>/', include([
        path('details/', views.DetailsAlbum.as_view(), name='album_details'),
        path('edit/', views.EditAlbum.as_view(), name='album_edit'),
        path('delete/', views.DeleteAlbum.as_view(), name='album_delete'),
    ])),
]