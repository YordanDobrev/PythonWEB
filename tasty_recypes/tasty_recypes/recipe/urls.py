from django.urls import path, include

from tasty_recypes.recipe import views

urlpatterns = [
    path('catalogue/', views.recipe_catalog, name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:id>/', include([
        path('details/', views.RecipeDetailView.as_view(), name='recipe_details'),
        path('edit/', views.recipe_edit, name='recipe_edit'),
        path('delete/', views.recipe_delete, name='recipe_delete'),
    ]))
]
