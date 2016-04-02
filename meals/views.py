from django.shortcuts import render
from django.http import HttpResponse
from meals.models import Recipe


# def search_form(request):
#     return render(request, 'search_form.html')
#
#
# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#
#         recipes = Recipe.objects.filter(meat=q)
#
#         # recipes = Recipe.objects.filter(name__icontains=q)
#         return render(request, 'search_results.html',
#             {'recipes': recipes, 'query': q})
#     else:
#         return HttpResponse('Please submit a search term.')
