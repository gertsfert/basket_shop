from recipes.serializers import *
from rest_framework import generics

from recipes.models import (
    IngredientType, Ingredient, Recipe, RecipeIngredient, RecipeStep)


class IngredientTypeListCreate(generics.ListCreateAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializers


class IngredientSerializers(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class RecipeIngredientSerializers(generics.ListCreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializers


class RecipeBrowseSerializers(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeBrowseSerializers


class RecipeDetailSerializers(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializers
    lookup_field = ('pk')
