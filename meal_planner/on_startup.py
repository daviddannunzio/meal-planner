from meals.models import Recipe
import json
import os
from django.conf import settings


def load(reset=False):
    # Clear the DB
    if reset:
        Recipe.objects.all().delete()

    existing = []
    for r in Recipe.objects.all():
        existing.append(r.name)


    directory = settings.BASE_DIR + '/meal_planner/recipes/'
    
    for recipe_file in os.listdir(directory):
        if recipe_file == 'recipes.json':
            continue

        json_data = open(os.path.join(directory, recipe_file))
        json_recipe = json.load(json_data)

        if json_recipe["name"] in existing:
            continue

        recipe = Recipe.objects.create(name=json_recipe["name"],
                                       meat=json_recipe["meat"],
                                       website=json_recipe["website"])

        for step in json_recipe["steps"]:
            recipe.recipestep_set.create(recipe=recipe,
                                         step_number=step["step_number"],
                                         step_description=step["step_description"])

        for ingredient in json_recipe["ingredients"]:
            recipe.ingredients_set.create(recipe=recipe,
                                          name=ingredient["name"],
                                          amount=ingredient["amount"],
                                          unit=ingredient["unit"],
                                          preparation=ingredient["preparation"])
