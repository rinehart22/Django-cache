from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'h.html')


def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipes.html', {
        'recipes': recipes
    })
