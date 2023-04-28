from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'date_posted', 'preparation_time_in_minutes', 'instructions', ]
