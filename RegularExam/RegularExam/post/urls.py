from django.urls import path, include

from RegularExam.post import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/', include([  #TO ASK IN SLIDO IF THIS IS A SLUG OR THE ID OF THE POST
        path('details/', views.details_post, name='details_post'),
        path('edit/', views.edit_post, name='edit_post'),
        path('delete/', views.delete_post, name='delete_post'),
    ])),
]
