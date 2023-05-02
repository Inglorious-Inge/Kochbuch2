from django.urls import path, include
from rest_framework import routers
from recipes.views import RecipeViewSet, favorites


router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('favorites', favorites)
]
