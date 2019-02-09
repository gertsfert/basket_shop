from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredienttype/', views.IngredientTypeListCreate.as_view()),
    path('api/ingredient/', views.IngredientSerializers.as_view()),
    path('api/recipieingredient/',
         views.RecipieIngredientSerializers.as_view()),
    path('api/recipie/', views.RecipieSerializers.as_view()),
]
