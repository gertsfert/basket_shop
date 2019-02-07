from rest_framework import serializers
from recipies.models import IngredientType, Ingredient, RecipieIngredient, RecipieStep, Recipie


class IngredientTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipieIngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipieIngredient
        fields = '__all__'


class RecipieStepSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipieStep
        fields = '__all__'


class RecipieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = '__all__'
