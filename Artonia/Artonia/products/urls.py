from django.urls import path
from Artonia.products.views import index

urlpatterns = [
    path('', index),
]