from datetime import datetime
from rest_framework import serializers

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics as rest_views

from server.api.serializers import RecipieSerializer
from server.recipies.models import Recipie


@api_view()
def recipie_list(request):
    recipies = Recipie.objects.all()
    recipies = list(recipies.values())
    serializer = RecipieSerializer(recipies)
    # print(serializer.data)
    return Response(serializer.data)


class RecipiesApiView(rest_views.ListAPIView):
    serializer_class = RecipieSerializer

    def get_queryset(self):
        queryset = Recipie.objects.all()
        return queryset


# @api_view()
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

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


serializer = CommentSerializer(comment)
print(serializer.data)
