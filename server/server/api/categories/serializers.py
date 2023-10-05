from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.recipies.models import Category

UserModel = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
