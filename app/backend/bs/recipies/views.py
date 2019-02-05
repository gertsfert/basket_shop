from recipies.models import IngredientType, Ingredient
from recipies.serializers import IngredientTypeSerializers
from recipies.serializers import IngredientSerializers
from rest_framework import generics


class IngredientTypeListCreate(generics.ListCreateAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializers


class IngredientSerializers(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
