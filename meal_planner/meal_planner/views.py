from django.shortcuts import render
from meals.models import Recipe
from on_startup import load


def index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']

        recipes = Recipe.objects.filter(meat=q)

        # recipes = Recipe.objects.filter(name__icontains=q)
        return render(request, 'home.html',
            {'recipe_list': recipes})
    else:
        load()
        return render(request, 'home.html', {'recipe_list': Recipe.objects.all().order_by("name")})


def recipe(request):
    return render(request, 'recipe.html', {'recipe' : Recipe.objects.get(id=request.GET['id'])})