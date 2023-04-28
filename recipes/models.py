from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now=True)
    preparation_time_in_minutes = models.PositiveIntegerField()
    instructions = models.TextField('Zubereitung', blank=True)
    ingredients = models.ManyToManyField('Ingredient', through='IngredientToRecipe')

    def __str__(self):
        return f" {self.title} - {self.date_posted} - {self.preparation_time_in_minutes} - {self.instructions} - "


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.ingredient


class IngredientToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200)


