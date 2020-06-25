from django.db import models

MEAT = (
    ('V', 'Veggie'),
    ('T', 'Tofu'),
    ('C', 'Chicken'),
    ('F', 'Fish'),
    ('B', 'Beef'),
    ('P', 'Pork'),
    ('VEGAN', 'Vegan'),
)


class Recipe(models.Model):
    name = models.CharField(max_length=500)
    website = models.CharField(max_length=5000)
    meat = models.CharField(max_length=5, choices=MEAT)

    def __unicode__(self):
        return self.name, self.recipestep_set.all()


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe)
    step_number = models.IntegerField()
    step_description = models.CharField(max_length=40000)

    def __unicode__(self):
        return self.step_description

    class Meta:
        ordering = ['step_number']


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=100)
    preparation = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s: %s %s' % (self.name, self.amount, self.unit)
