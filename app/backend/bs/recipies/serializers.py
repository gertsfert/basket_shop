from rest_framework import serializers
from recipies.models import IngredientType, Ingredient


class IngredientTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
