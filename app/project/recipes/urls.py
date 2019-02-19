from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredienttype/', views.IngredientTypeListCreate.as_view()),
    path('api/ingredient/', views.IngredientViewSet.as_view()),
    path('api/recipes/', views.RecipeBrowseViewSet.as_view()),
    path('api/recipe/<int:pk>/', views.RecipeDetailViewSet.as_view()),
]
