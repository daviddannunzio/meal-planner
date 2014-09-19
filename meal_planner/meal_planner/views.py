from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from meals.models import Recipe, Ingredients
from on_startup import load
from forms import RecipeForm


def determine_meat(form, recipes):
    meat = form.cleaned_data.get('meat')

    if meat:
        recipes = recipes.filter(meat__in=meat)

    return recipes


def determine_max_ingredients(form, recipes):
    max_ingredients = form.cleaned_data.get('max_ingredients')
    recipes_with_too_many_ingredients = []

    for recipe in recipes:
        ingredients = Ingredients.objects.filter(recipe__id=recipe.id)
        if len(ingredients) > max_ingredients:
            recipes_with_too_many_ingredients.append(recipe.id)

    recipes = recipes.exclude(id__in=recipes_with_too_many_ingredients)

    return recipes

FILTER_METHODS = [determine_meat, determine_max_ingredients]


def index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipes = Recipe.objects.all().order_by("name")

            for filter_method in FILTER_METHODS:
                recipes = filter_method(form, recipes)

            return render(request, 'home.html', {'form': form, 'recipe_list': recipes})

    else:
        load()
        form = RecipeForm

    return render_to_response('home.html', {'form': form, 'recipe_list': Recipe.objects.all().order_by("name")},
                              context_instance=RequestContext(request))


def recipe(request):
    return render(request, 'recipe.html', {'recipe': Recipe.objects.get(id=request.GET['id'])})


def export(request):
    ingredients_file = open('/Users/David/Downloads/ingredients.txt', 'w')
    for ingredient in Recipe.objects.get(id=request.GET['id']).ingredients_set.all():
        ingredients_file.write(" ".join([str(ingredient.name), str(ingredient.amount), str(ingredient.unit)]) + "\n")

    ingredients_file.close()
    return redirect('/recipe/?id=' + request.GET['id'])