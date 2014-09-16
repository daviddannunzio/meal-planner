from django import forms
from meals.models import MEAT


class RecipeForm(forms.Form):
    meat = forms.MultipleChoiceField(choices=MEAT,
                                     required=False,
                                     widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'this.form.submit();'}))