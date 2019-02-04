from django.db import models
from django.db.models import CASCADE


class IngredientType(models.Model):
    # fruit/veg; canned; meat; etc
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    ingredient_type = models.ForeignKey(IngredientType, on_delete=CASCADE)
    shelf_life = models.DurationField()


class Recipie(models.Model):
    introduction = models.TextField()
    photo = models.ImageField(upload_to='recipie_photos')
    serves = models.PositiveSmallIntegerField()


class RecipieStep(models.Model):
    recipie = models.ForeignKey(Recipie, on_delete=CASCADE)
    number = models.PositiveSmallIntegerField()
    text = models.TextField()


class RecipieIngredient(models.Model):
    recipie = models.ForeignKey(Recipie, on_delete=CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=50)
    adjective = models.CharField(max_length=100)
    notes = models.CharField(max_length=240)
