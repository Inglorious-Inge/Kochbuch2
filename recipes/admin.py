from django.contrib import admin
from .models import Recipe, Ingredient, IngredientToRecipe, Favorite, Search, ShoppingList, RecipeToShoppinglist


class IngredientToRecipeInLine(admin.TabularInline):
    model = IngredientToRecipe
    extra = 1


class FavoriteInLine(admin.TabularInline):
    model = Favorite
    extra = 1


class SearchAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientToRecipeInLine, FavoriteInLine]


class FavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,)
admin.site.register(IngredientToRecipe)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(ShoppingList)
admin.site.register(RecipeToShoppinglist)


