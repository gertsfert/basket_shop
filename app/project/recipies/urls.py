from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredienttype/', views.IngredientTypeListCreate.as_view()),
    path('api/ingredient/', views.IngredientSerializers.as_view()),
    path('api/recipieingredient/',
         views.RecipieIngredientSerializers.as_view()),
    path('api/recipies/', views.RecipieBrowseSerializers.as_view()),
    path('api/recipie/<int:pk>/', views.RecipieDetailSerializers.as_view()),
]
