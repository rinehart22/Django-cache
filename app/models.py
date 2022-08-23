from django.db import models

# Create your models here.
class Recipe(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(
        'app.Meal',
        through='app.Ingredient',
        through_fields=('recipe', 'meal')
    )

    instructions = models.TextField(null=True, blank=True)

    class Meta(object):
        app_label = 'app'
        default_related_name = 'recipes'

    def __str__(self):
        return self.name


class Meal(models.Model):
    """An edible item."""

    name = models.CharField(max_length=255)

    class Meta(object):
        app_label = 'app'
        default_related_name = 'meals'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """A meal that is used in a recipe."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    # ex. 1/8 = 0.125, 1/4 = 0.250
    amount = models.DecimalField(max_digits=6, decimal_places=3,
                                 null=True, blank=True)
    # ex. tsp, tbsp, cup
    unit_of_measure = models.CharField(max_length=255)
    # ex. 2 cloves of garlic, minced
    description = models.TextField()

    class Meta(object):
        app_label = 'app'

    def __str__(self):
        return '{recipe}: {amount} {unit_of_measure} {meal}'.format(
            recipe=self.recipe,
            amount=self.amount,
            unit_of_measure=self.unit_of_measure,
            meal=self.meal
        )
