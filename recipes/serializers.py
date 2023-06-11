from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'created_by', 'image', 'preparation_time_in_minutes', 'serving_size', 'instructions',
                  'level', 'tags', ]
