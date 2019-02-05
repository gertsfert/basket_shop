from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredienttype/', views.IngredientTypeListCreate.as_view()),
    path('api/ingredient/', views.IngredientSerializers.as_view())
]