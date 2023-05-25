from django.urls import path, include
from rest_framework import routers
from recipes.views import RecipeViewSet, favorites, search, shoppinglists, shoppinglist_detail

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('recipes/search/', search),
    path('', include(router.urls)),
    path('favorites/', favorites),
    path('shoppinglists/', shoppinglists),
    path('shoppinglists/<int:shoppinglist_id>/', shoppinglist_detail)

]
