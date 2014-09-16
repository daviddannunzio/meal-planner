from django.shortcuts import render, render_to_response
from django.template import RequestContext
from meals.models import Recipe
from on_startup import load
from forms import RecipeForm

def index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            meat = form.cleaned_data.get('meat')

            if not meat:
                return render(request, 'home.html', {'form': form, 'recipe_list': Recipe.objects.all().order_by("name")})

            recipes = Recipe.objects.filter(meat__in=meat)

            return render(request, 'home.html', {'form': form, 'recipe_list': recipes})

    else:
        load()
        form = RecipeForm

    return render_to_response('home.html', {'form': form, 'recipe_list': Recipe.objects.all().order_by("name")},
                              context_instance=RequestContext(request))


def recipe(request):
    return render(request, 'recipe.html', {'recipe' : Recipe.objects.get(id=request.GET['id'])})