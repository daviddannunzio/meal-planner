from meals.models import Recipe
import json

def load():
    # Clear the DB
    Recipe.objects.all().delete()

    json_data = open('/Users/David/Desktop/meal_planner/meal_planner/meal_planner/recipes.json')
    recipes = json.load(json_data)

    for json_recipe in recipes:
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
    Recipe.objects.create(name="Simple Red Split Lentils",
                          meat="V",
                          website="http://www.wikihow.com/Cook-Red-Split-Lentils")
    Recipe.objects.create(name="The Best Roasted Vegetables Ever",
                          meat="V",
                          website="http://www.thewednesdaychef.com/the_wednesday_chef/2013/07/the-best-roasted-vegetables-ever.html")
    Recipe.objects.create(name="Potato Frittata",
                          meat="V",
                          website="http://www.bhg.com/recipe/potato-frittata/")
    Recipe.objects.create(name="Cast Iron Skillet Spinach Mushroom Frittata",
                          meat="V",
                          website="http://www.honeywhatscooking.com/2013/02/cast-iron-skillet-spinach-mushroom.html")
    Recipe.objects.create(name="Simple Black Bean Burgers",
                          meat="V",
                          website="http://www.foodnetwork.com/recipes/sandra-lee/black-bean-burgers-recipe.html")
    Recipe.objects.create(name="Asian Beef Skewers",
                          meat="B",
                          website="http://www.food.com/recipe/asian-beef-skewers-3-points-169074")
    Recipe.objects.create(name="Beef Fajitas",
                          meat="B",
                          website="http://thepioneerwoman.com/cooking/2013/03/beef-fajitas/")
    Recipe.objects.create(name="Honey Soy Grilled Salmon with Edamame",
                          meat="F",
                          website="http://www.foodnetwork.com/recipes/food-network-kitchens/honey-soy-grilled-salmon-with-edamame-recipe.html")
    Recipe.objects.create(name="Slow Cooker Beef Stew",
                          meat="B",
                          website="http://allrecipes.com/recipe/slow-cooker-beef-stew-i/")
    Recipe.objects.create(name="Boursin and Spinach Stuffed Chicken",
                          meat="C",
                          website="http://lifeonfood.blogspot.com/2011/12/boursin-and-spinach-stuffed-chicken.html")
    Recipe.objects.create(name="Thai Style Halibut with Coconut Curry Broth",
                          meat="F",
                          website="http://www.foodnetwork.com/recipes/ellie-krieger/thai-style-halibut-with-coconut-curry-broth-recipe.html")
    Recipe.objects.create(name="Moroccan Spiced Chickpea Carrot Soup",
                          meat="V",
                          website="http://cookbakenibble.com/2011/03/02/moroccan-spiced-chickpea-carrot-soup/")
    Recipe.objects.create(name="Beef Stuffed Sweet Potato",
                          meat="B",
                          website="http://www.foodnetwork.com/recipes/food-network-kitchens/beefy-stuffed-sweet-potato.html")
    Recipe.objects.create(name="Fall Veggie and Quinoa Hash Poached Eggs",
                          meat="V",
                          website="http://www.wholeliving.com/132622/fall-vegetable-and-quinoa-hash-poached-eggs")
    Recipe.objects.create(name="Sage and Garlic Roasted Chicken, Pomegranate Glaze",
                          meat="C",
                          website="http://www.insockmonkeyslippers.com/sage-and-garlic-roasted-chicken-with-pomegranate-and-black-pepper-glaze")
    Recipe.objects.create(name="Lentils and Sausage braised in Red Wine",
                          meat="P",
                          website="http://www.biggirlssmallkitchen.com/2013/01/lentils-and-sausage-braised-in-red-wine.html")
    Recipe.objects.create(name="Meatball Pizza on Naan",
                          meat="B",
                          website="http://www.biggirlssmallkitchen.com/2014/03/meatball-pizza-on-a-naan-crust.html")
    Recipe.objects.create(name="Squash Coconut Curry",
                          meat="V",
                          website="http://pinchofyum.com/30-minute-squash-coconut-curry")
    Recipe.objects.create(name="Healthy Mac and Cheese",
                          meat="V",
                          website="http://pinchofyum.com/healthy-mac-and-cheese")
    Recipe.objects.create(name="Farfalle with Mushrooms and Spinach",
                          meat="V",
                          website="http://www.bhg.com/recipe/pasta/farfalle-with-mushrooms-and-spinach/")
    Recipe.objects.create(name="Avocado Mango Chicken Salad",
                          meat="C",
                          website="http://eat-drink-love.com/2013/02/avocado-mango-chicken-salad/")
    Recipe.objects.create(name="Mango Avocado Salsa on Salmon",
                          meat="F",
                          website="http://nomnompaleo.com/post/56076300574/mango-avocado-salsa-on-pan-seared-salmon")
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
    Recipe.objects.create(name="Fish with Lemon and Caper Sauce",
                          meat="F",
                          website="http://www.williams-sonoma.com/recipe/fish-with-lemon-and-caper-sauce.html")
    Recipe.objects.create(name="Spicy Black Bean Cakes",
                          meat="V",
                          website="http://www.marthastewart.com/332312/spicy-black-bean-cakes")
    Recipe.objects.create(name="Sweet Mustard Chicken Thighs",
                          meat="C",
                          website="http://www.myrecipes.com/recipe/sweet-mustard-chicken-thighs-10000001896116/")
    '''