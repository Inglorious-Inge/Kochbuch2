from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import IngredientToRecipe
from .models import Favorite


class IngredientToRecipeInLine(admin.TabularInline):
    model = IngredientToRecipe
    extra = 1


class FavoriteInLine(admin.TabularInline):
    model = Favorite
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientToRecipeInLine, FavoriteInLine]


class FavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,)
admin.site.register(IngredientToRecipe)
admin.site.register(Favorite, FavoriteAdmin)


