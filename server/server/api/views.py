from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from rest_framework import generics as rest_views, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from server.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from server.api.serializers import RecipiesSerializer, RecipieSerializer, ReviewSerializer, CreateReviewSerializer, \
    CategorySerializer, CommentSerializer, PhotoSerializer, UserSerializer, EditExtendAppUserSerializer
from server.recipies.models import Recipie, Review, Category, Comment, Photo
from server.user_app.models import ExtendAppUser

UserModel = get_user_model()


# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# @api_view(['GET', 'POST'])
# def recipie_list(request):
#     if request.method == 'GET':
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def recipie_details(request, pk):
#     try:
#         recipie = Recipie.objects.filter(pk=pk).get()
#     except Recipie.DoesNotExist:
#         return Response({'error': 'recipie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ListRecipiesAV(APIView):
#
#     def get(self, request):
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class DetailsRecipieAV(APIView):
#
#     def get(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)















