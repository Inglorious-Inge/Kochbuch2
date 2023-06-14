from rest_framework import serializers
from recipes.models import Recipe, ShoppingList, IngredientToRecipe, RecipeToShoppinglist


class IngredientToRecipeSerializer(serializers.ModelSerializer):
    ingredient_id = serializers.SlugRelatedField(slug_field='ingredient', read_only=True)

    class Meta:
        model = IngredientToRecipe
        fields = ['amount', 'unit', 'ingredient_id']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientToRecipeSerializer(many=True, source='ingredienttorecipe_set')

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'created_by', 'image', 'preparation_time_in_minutes', 'serving_size', 'instructions',
                  'level', 'tags', 'ingredients']


class ShoppingListSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)
    cumulated_ingredients = serializers.SerializerMethodField()

    def get_cumulated_ingredients(self, obj):
        cumulated_ingredients = {}  # dictionary
        recipe_ids = RecipeToShoppinglist.objects.filter(shoppinglist_id=obj.id).values_list("recipe_id", flat=True)
        ingredient_to_recipes = IngredientToRecipe.objects.filter(recipe_id__in=recipe_ids).order_by('ingredient_id__ingredient')
        for itr in ingredient_to_recipes:
            if (itr.ingredient_id.ingredient, itr.unit) not in cumulated_ingredients:
                cumulated_ingredients[(itr.ingredient_id.ingredient, itr.unit)] = itr.amount
            else:
                cumulated_ingredients[(itr.ingredient_id.ingredient, itr.unit)] += itr.amount

        results = []  # list
        for key, value in cumulated_ingredients.items():
            results.append(
                {
                    "ingredient": key[0],
                    "unit": key[1],
                    "amount": cumulated_ingredients[key],
                }
            )
        return results

    class Meta:
        model = ShoppingList
        fields = ['title', 'recipes', 'cumulated_ingredients']
