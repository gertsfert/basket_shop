from rest_framework import serializers
from recipes.models import (IngredientType, Ingredient, RecipeIngredient,
                            RecipeStep, Recipe)


class IngredientTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    ingredient_type = IngredientTypeSerializers(read_only=True)

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeIngredientSerializers(serializers.ModelSerializer):
    ingredient = IngredientSerializers(read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'ingredient', 'quantity', 'unit',
                  'adjective', 'notes')


class RecipeStepSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ('id', 'number', 'text')


class RecipeDetailSerializers(serializers.ModelSerializer):
    """
    Returns the details of the recipe
    """
    steps = RecipeStepSerializers(many=True, read_only=True)
    ingredients = RecipeIngredientSerializers(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'introduction',
                  'serves', 'ingredients', 'steps')


class RecipeBrowseSerializers(serializers.ModelSerializer):
    """
    Returns all recipes for a browse view
    """
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'introduction',
                  'serves')
