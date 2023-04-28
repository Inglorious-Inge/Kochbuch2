from django.shortcuts import render
from rest_framework import viewsets, permissions
from recipes.serializers import RecipeSerializer
from .models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [permissions.AllowAny]
