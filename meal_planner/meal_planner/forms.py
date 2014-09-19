from django import forms
from meals.models import MEAT


class RecipeForm(forms.Form):
    meat = forms.MultipleChoiceField(choices=MEAT,
                                     required=False,
                                     widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'this.form.submit();'}))
    max_ingredients = forms.IntegerField(label="Max Number of Ingredients",
                                         initial=50,
                                         min_value=1,
                                         max_value=50,
                                         widget=forms.NumberInput(attrs={'onchange': 'this.form.submit();'}))


class OwnedIngredientsForm(forms.Form):
    owned_ingredients = {}

    def __init__(self, ingredients):
        for ingredient in ingredients:
            self.owned_ingredients.append(forms.BooleanField(initial=False))
