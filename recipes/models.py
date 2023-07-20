from django.db import models
from django.db.models import Q  # A Q object describes a part of an SQL query
from django.contrib.auth import get_user_model
from django.db.models.functions import Lower
from django.db.models import Count

LEVELS = (
    ('easy', 'leicht'),
    ('medium', 'mittel'),
    ('hard', 'schwer')
)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name="recipes_created")
    image = models.ImageField(upload_to='recipe_images', blank=True)
    preparation_time_in_minutes = models.PositiveIntegerField()
    instructions = models.TextField('Zubereitung')
    ingredients = models.ManyToManyField('Ingredient', through='IngredientToRecipe')
    level = models.CharField(max_length=6, choices=LEVELS)
    serving_size = models.PositiveIntegerField()
    favored_by = models.ManyToManyField(get_user_model(), through='Favorite', related_name="recipes_favored")
    tags = models.ManyToManyField('Tag', through='TagToRecipe', blank=True)

    def __str__(self):
        return f" {self.title} - {self.preparation_time_in_minutes} - {self.level} - {self.tags} - "

    def find_similar_recipes(self):
        same_tag = Q(tags__in=self.tags.all())
        has_shared_ingredients = Q(ingredients__in=self.ingredients.all())
        same_tag_and_at_least_two_shared_ingredients = Recipe.objects.filter(same_tag & has_shared_ingredients).annotate(
            shared_ingredients=Count("ingredients")
        ).filter(shared_ingredients__gte=2)
        at_least_four_shared_ingredients = Recipe.objects.filter(has_shared_ingredients).annotate(
            shared_ingredients=Count("ingredients")
        ).filter(shared_ingredients__gte=4)
        similar_recipes = at_least_four_shared_ingredients | same_tag_and_at_least_two_shared_ingredients
        # similar_recipes = at_least_four_shared_ingredients.exclude(id=self.id).union(
        #    same_tag_and_at_least_two_shared_ingredients.exclude(id=self.id))
        # breakpoint()
        similar_recipes = similar_recipes.exclude(id=self.id)
        return similar_recipes.distinct()
        # return similar_recipes


class Search(models.Model):
    """Model to save search requests"""
    title = models.CharField(max_length=200, blank=True)
    preparation_time_in_minutes_max = models.PositiveIntegerField(blank=True, null=True)
    level = models.CharField(max_length=6, choices=LEVELS, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f" {self.title} - {self.preparation_time_in_minutes_max} - {self.level} - {self.tags} - "


class IngredientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).order_by(Lower('ingredient'))


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=200, unique=True)
    objects = IngredientManager()

    def __str__(self):
        return self.ingredient


class TagManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).order_by(Lower('tag'))


class Tag(models.Model):
    tag = models.CharField(max_length=200, unique=True)
    objects = TagManager()

    def __str__(self):
        return self.tag


class ShoppingList(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.title} "


class ShoppingListIngredient(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    is_bought = models.BooleanField(default=False)
    objects = IngredientManager()

    class Meta:
        unique_together = [
            ('ingredient', 'unit', 'shopping_list')
        ]

    def __str__(self):
        return f'{self.shopping_list}: {self.ingredient} ({self.unit})'


class TagToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.tag_id} to {self.recipe_id.title}"


class IngredientToRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200)

    def __str__(self):
        return f" {self.amount} {self.unit} {self.ingredient_id} added to {self.recipe_id.title}"


class Favorite(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.user_id} added {self.recipe_id.title} "




