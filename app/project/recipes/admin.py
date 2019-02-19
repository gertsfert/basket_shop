from django.contrib import admin

from .models import (IngredientType, Ingredient, Recipe,
                     RecipeStep, RecipeIngredient)

admin.site.register([IngredientType, Ingredient, Recipe,
                     RecipeStep, RecipeIngredient])

# Register your models here.
