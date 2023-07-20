from django.contrib import admin
from .models import (Recipe, Ingredient, IngredientToRecipe, Favorite, Search, ShoppingList, ShoppingListIngredient,
                     Tag, TagToRecipe)


class IngredientToRecipeInLine(admin.TabularInline):
    model = IngredientToRecipe
    extra = 1


class ShoppingListIngredientInLine(admin.TabularInline):
    model = ShoppingListIngredient
    extra = 1

class FavoriteInLine(admin.TabularInline):
    model = Favorite
    extra = 1


class TagToRecipeInLine(admin.TabularInline):
    model = TagToRecipe
    extra = 1


class SearchAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientToRecipeInLine, FavoriteInLine, TagToRecipeInLine]


class ShoppinglistAdmin(admin.ModelAdmin):
    inlines = [ShoppingListIngredientInLine]


class ShoppingListIngredientAdmin(admin.ModelAdmin):
    pass

class FavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, )
admin.site.register(IngredientToRecipe)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(ShoppingList, ShoppinglistAdmin)
admin.site.register(ShoppingListIngredient, ShoppingListIngredientAdmin)
admin.site.register(Tag)
admin.site.register(TagToRecipe)
