from rest_framework import serializers
from recipes.models import Recipe, ShoppingList, ShoppingListIngredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'created_by', 'image', 'preparation_time_in_minutes', 'serving_size', 'instructions',
                  'level', 'tags', ]

class ShoppingListIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingListIngredient
        fields = ['ingredient', 'unit', 'amount', 'is_bought', ]

class ShoppingListSerializer(serializers.ModelSerializer):

    ingredients = ShoppingListIngredientSerializer(many=True)
    class Meta:
        model = ShoppingList
        fields = ['id', 'title', 'user', 'ingredients']