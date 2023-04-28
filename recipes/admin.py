from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import IngredientToRecipe


class IngredientToRecipeInLine(admin.TabularInline):
    model = IngredientToRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientToRecipeInLine]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,)
admin.site.register(IngredientToRecipe)


