# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import JsonResponse
# from server.recipies.models import Recipie
#
#
# def recipie_list(request):
#     recipies = Recipie.objects.all()
#     data = {'recipies': list(recipies.values())}
#     return JsonResponse(data)
#
#
# def recipie_details(request, pk):
#     try:
#         recipie = Recipie.objects.filter(pk=pk).get()
#     except Recipie.DoesNotExist:
#         return JsonResponse({'alert': "no recipie found"})
#
#     data = {
#         'title': recipie.title,
#         'description': recipie.description,
#         'ingredients': recipie.ingredients,
#         'preparation': recipie.preparation,
#         'preparation_time': recipie.preparation_time,
#         'cooking_time': recipie.cooking_time,
#         'portions': recipie.portions,
#     }
#     return JsonResponse(data)
