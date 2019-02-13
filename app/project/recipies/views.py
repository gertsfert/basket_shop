from recipies.serializers import *
from rest_framework import generics

from recipies.models import (
    IngredientType, Ingredient, Recipie, RecipieIngredient, RecipieStep)


class IngredientTypeListCreate(generics.ListCreateAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializers


class IngredientSerializers(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class RecipieIngredientSerializers(generics.ListCreateAPIView):
    queryset = RecipieIngredient.objects.all()
    serializer_class = RecipieIngredientSerializers


class RecipieBrowseSerializers(generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieBrowseSerializers
