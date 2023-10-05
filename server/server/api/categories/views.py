from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views

from server.api.permissions import AdminOrReadOnly
from server.api.categories.serializers import CategorySerializer
from server.recipies.models import Category

UserModel = get_user_model()


class CategoriesApiView(rest_views.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminOrReadOnly]


class CategoriesApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]
