from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images', blank=True)
    preparation_time_in_minutes = models.PositiveIntegerField()
    instructions = models.TextField('Zubereitung', blank=True)
    ingredients = models.ManyToManyField('Ingredient', through='IngredientToRecipe')
    favored_by = models.ManyToManyField(get_user_model(),through='Favorite')

    def __str__(self):
        return f" {self.title} - {self.date_posted} - {self.preparation_time_in_minutes} - {self.instructions} - "


class Favorite(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.ingredient


class IngredientToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200)


