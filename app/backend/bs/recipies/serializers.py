from rest_framework import serializers
from recipies.models import (IngredientType, Ingredient, RecipieIngredient,
                             RecipieStep, Recipie)


class IngredientTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    ingredient_type = IngredientTypeSerializers(read_only=True)

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipieIngredientSerializers(serializers.ModelSerializer):
    ingredient = IngredientSerializers(read_only=True)

    class Meta:
        model = RecipieIngredient
        fields = ('id', 'ingredient', 'quantity', 'unit',
                  'adjective', 'notes')


class RecipieStepSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipieStep
        fields = ('id', 'number', 'text')


class RecipieSerializers(serializers.ModelSerializer):
    """
    Returns the details of the recipie
    """
    steps = RecipieStepSerializers(many=True, read_only=True)
    ingredients = RecipieIngredientSerializers(many=True, read_only=True)

    class Meta:
        model = Recipie
        fields = ('id', 'name', 'introduction',
                  'serves', 'ingredients', 'steps')
