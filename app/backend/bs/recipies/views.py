from recipies.models import IngredientType, Ingredient
from recipies.serializers import *
from rest_framework import generics


class IngredientTypeListCreate(generics.ListCreateAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializers


class IngredientSerializers(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class RecipieIngredientSerializers(generics.ListCreateAPIView):
    queryset = RecipieIngredient.objects.all()
    serializer_class = RecipieIngredientSerializers


class RecipieStepSerializers(generics.ListCreateAPIView):
    queryset = RecipieStep.objects.all()
    serializer_class = RecipieStepSerializers


class RecipieSerializers(generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializers
