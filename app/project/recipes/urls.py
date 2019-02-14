from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredienttype/', views.IngredientTypeListCreate.as_view()),
    path('api/ingredient/', views.IngredientSerializers.as_view()),
    path('api/recipeingredient/',
         views.RecipeIngredientSerializers.as_view()),
    path('api/recipes/', views.RecipeBrowseSerializers.as_view()),
    path('api/recipe/<int:pk>/', views.RecipeDetailSerializers.as_view()),
]
