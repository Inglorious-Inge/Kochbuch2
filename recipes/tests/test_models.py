from django.test import TestCase
from recipes.models import Ingredient, IngredientToRecipe, Recipe, Tag


class TestRecipe(TestCase):

    def setUp(self):
        tag = Tag.objects.create(tag="test-tag")
        self.recipe = Recipe.objects.create(
            title="Test-Recipe",
            preparation_time_in_minutes=10,
            serving_size=2,
        )
        self.recipe.tags.add(tag)
        self.same_tag_and_two_shared_ingredients = Recipe.objects.create(
            title="Same Tag and two shared Ingredients",
            preparation_time_in_minutes=10,
            serving_size=2,
        )
        self.same_tag_and_two_shared_ingredients.tags.add(tag)
        sugar = Ingredient.objects.create(ingredient="Sugar")
        flour = Ingredient.objects.create(ingredient="Flour")
        IngredientToRecipe.objects.create(recipe_id=self.recipe, ingredient_id=sugar, amount=1, unit="g")
        IngredientToRecipe.objects.create(recipe_id=self.recipe, ingredient_id=flour, amount=2, unit="g")
        IngredientToRecipe.objects.create(
            recipe_id=self.same_tag_and_two_shared_ingredients,
            ingredient_id=sugar,
            amount=1,
            unit="g"
        )
        IngredientToRecipe.objects.create(
            recipe_id=self.same_tag_and_two_shared_ingredients,
            ingredient_id=flour,
            amount=2,
            unit="g"
        )

    def test_find_similar_recipes(self):
        similar_recipes = self.recipe.find_similar_recipes()
        self.assertEquals(len(similar_recipes), 1)
