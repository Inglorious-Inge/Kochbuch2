from django.db import models
from django.contrib.auth import get_user_model

LEVELS = (
    ('easy', 'leicht'),
    ('medium', 'mittel'),
    ('hard', 'schwer')
)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='recipe_images', blank=True)
    preparation_time_in_minutes = models.PositiveIntegerField()
    instructions = models.TextField('Zubereitung')
    ingredients = models.ManyToManyField('Ingredient', through='IngredientToRecipe')
    level = models.CharField(max_length=6, choices=LEVELS)
    serving_size = models.PositiveIntegerField()
    favored_by = models.ManyToManyField(get_user_model(), through='Favorite')
    tags = models.ManyToManyField('Tag', through='TagToRecipe', blank=True)

    def __str__(self):
        return f" {self.title} - {self.date_posted} - {self.preparation_time_in_minutes} - {self.level} - {self.tags} - "


class Search(models.Model):
    title = models.CharField(max_length=200, blank=True)
    preparation_time_in_minutes_max = models.PositiveIntegerField(blank=True, null=True)
    level = models.CharField(max_length=6, choices=LEVELS, blank=True)
    tags = models.CharField(max_length=200, blank=True)


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.ingredient


class Tag(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class ShoppingList(models.Model):
    title = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, through='RecipeToShoppinglist')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class TagToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class RecipeToShoppinglist(models.Model):
    shoppinglist_id = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class IngredientToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200)


class Favorite(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)




