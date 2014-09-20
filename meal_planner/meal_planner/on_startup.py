from meals.models import Recipe
import json
import os


def load():
    # Clear the DB
    Recipe.objects.all().delete()

    directory = '/Users/David/Desktop/meal_planner/meal_planner/meal_planner/recipes/'
    for recipe_file in os.listdir(directory):
        if recipe_file == 'recipes.json':
            continue

        json_data = open(os.path.join(directory, recipe_file))
        json_recipe = json.load(json_data)

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

    # Load all recipes so far
    '''
    Recipe.objects.create(name="Lentils and Sausage braised in Red Wine",
                          meat="P",
                          website="http://www.biggirlssmallkitchen.com/2013/01/lentils-and-sausage-braised-in-red-wine.html")
    Recipe.objects.create(name="Meatball Pizza on Naan",
                          meat="B",
                          website="http://www.biggirlssmallkitchen.com/2014/03/meatball-pizza-on-a-naan-crust.html")
    Recipe.objects.create(name="Squash Coconut Curry",
                          meat="V",
                          website="http://pinchofyum.com/30-minute-squash-coconut-curry")
    Recipe.objects.create(name="Avocado Mango Chicken Salad",
                          meat="C",
                          website="http://eat-drink-love.com/2013/02/avocado-mango-chicken-salad/")
    Recipe.objects.create(name="Flavorful Chicken Fajitas",
                          meat="C",
                          website="http://www.tasteofhome.com/recipes/flavorful-chicken-fajitas")
    Recipe.objects.create(name="Thai Chicken Quinoa Bowl",
                          meat="C",
                          website="http://www.howsweeteats.com/2013/02/thai-chicken-quinoa-bowl/")
    Recipe.objects.create(name="Maple Tossed Rhubarb Puy Salad",
                          meat="V",
                          website="http://www.greenkitchenstories.com/maple-tossed-rhubarb-puy-salad/")
    Recipe.objects.create(name="Sweet Potato Chickpea Veggie Burger",
                          meat="V",
                          website="http://www.cooksmarts.com/cs-blog/2013/05/sweet-potato-chickpea-veggie-burger-patty-recipe/#.U-lVxI1dVPx")
    Recipe.objects.create(name="Spicy Black Bean Cakes",
                          meat="V",
                          website="http://www.marthastewart.com/332312/spicy-black-bean-cakes")
    '''