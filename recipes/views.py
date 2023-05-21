from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipes.serializers import RecipeSerializer
from .models import Recipe, ShoppingList


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [permissions.AllowAny]


@api_view()
def favorites(request):
    favs = request.user.favorite_set.all()  # Alles gut, kann so bleiben
    favs_list = []
    for fav in favs:
        favs_list.append(fav.recipe_id_id)

    return Response(favs_list)


@api_view()
def search(request):
    title = request.query_params.get('title')
    preparation_time_max = request.query_params.get('preparation_time_max')

    if preparation_time_max is not None:
        preparation_time_max = int(preparation_time_max)
        results = Recipe.objects.filter(preparation_time_in_minutes__lte=preparation_time_max)
        # lte = less than or equal
        # linke Seite = Modelfeld / rechte Seite = Suchwert
    elif title is not None:
        results = Recipe.objects.filter(title__icontains=title)  # icontains = Case insensitive + contains
    else:
        results = Recipe.objects.all()

    serialised_results = []
    for result in results:
        serializer = RecipeSerializer(result)
        new_result = serializer.data  # Umbenennung zur besseren Lesbarkeit
        serialised_results.append(new_result)

    return Response(serialised_results)


@api_view()
def shoppinglists(request):
    lists = request.user.shoppinglist_set.all()  #  Passt so
    shoppinglists = []
    for list in lists:
        shoppinglists.append(list.title)

    return Response(shoppinglists)


@api_view()
def shoppinglist_detail(request, shoppinglist_id):
    shoppinglist = ShoppingList.objects.get(id=shoppinglist_id)
    title = shoppinglist.title

    return Response(title)
