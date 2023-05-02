from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipes.serializers import RecipeSerializer
from .models import Recipe
from .models import Favorite


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [permissions.AllowAny]

@api_view()
def favorites(request):
    favs = request.user.favorite_set.all()
    favs_list = []
    for fav in favs:
        favs_list.append(fav.recipe_id_id)

    return Response(favs_list)
