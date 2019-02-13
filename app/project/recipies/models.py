from django.db import models
from django.db.models import CASCADE


class IngredientType(models.Model):
    def __str__(self):
        return self.name

    # fruit/veg; canned; meat; etc
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    ingredient_type = models.ForeignKey(
        IngredientType, on_delete=CASCADE, related_name='ingredient')
    shelf_life = models.DurationField(blank=True)


class Recipie(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    introduction = models.TextField()
    photo = models.ImageField(upload_to='recipie_photos', blank=True)
    serves = models.PositiveSmallIntegerField()


class RecipieStep(models.Model):
    recipie = models.ForeignKey(
        Recipie, on_delete=CASCADE, related_name='steps')
    number = models.PositiveSmallIntegerField()
    text = models.TextField()


class RecipieIngredient(models.Model):
    recipie = models.ForeignKey(
        Recipie, on_delete=CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(
        Ingredient, on_delete=CASCADE, related_name='recipie_ingredient')
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    adjective = models.CharField(max_length=100)
    notes = models.CharField(max_length=240)
