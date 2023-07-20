from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipes.serializers import RecipeSerializer, ShoppingListSerializer
from .models import Recipe, ShoppingList


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@api_view()
def favorites(request):
    favs = request.user.favorite_set.all()  # okay
    favs_list = []
    for fav in favs:
        favs_list.append(fav.recipe_id_id)

    return Response(favs_list)


@api_view()
def search(request):
    title = request.query_params.get('title')
    preparation_time_max = request.query_params.get('preparation_time_max')
    level = request.query_params.get('levels')
    tags = request.query_params.get('tags')
    tag_relation = request.query_params.get('tag_relation', 'and')  # 'and' as default if not provided
    search_results = Recipe.objects.all()  # QuerySet

    if title is not None:
        search_results = search_results.filter(title__icontains=title)  # icontains = Case insensitive + contains
    if preparation_time_max is not None:
        preparation_time_max = int(preparation_time_max)
        search_results = search_results.filter(preparation_time_in_minutes__lte=preparation_time_max)
        # lte = less than or equal
        # linke Seite = Modelfeld / rechte Seite = Suchwert
    if level is not None:
        search_results = search_results.filter(level__iexact=level)  # besser möglich?
    if tags is not None:
        tag_list = [tag.strip() for tag in tags.split(',')]
        if tag_relation == 'and':  # 'and' = all the tags
            for tag in tag_list:
                search_results = search_results.filter(tags__tag=tag)
        if tag_relation == 'or':  # 'or' = at least one of the tags
            search_results = search_results.filter(tags__tag__in=tag_list)

    search_results = search_results.distinct()

    serialised_results = []
    for result in search_results:
        serializer = RecipeSerializer(result)
        new_result = serializer.data  # renaming for readability
        serialised_results.append(new_result)

    return Response(serialised_results)


@api_view()
def shoppinglists(request):
    lists = request.user.shoppinglist_set.all()  #  okay
    serializer = ShoppingListSerializer(lists, many=True)
    return Response(serializer.data)


@api_view()
def shoppinglist_detail(request, shoppinglist_id):
    shoppinglist = ShoppingList.objects.get(id=shoppinglist_id)
    serializer = ShoppingListSerializer(shoppinglist)
    return Response(serializer.data)

