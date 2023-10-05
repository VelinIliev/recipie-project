from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.recipies.models import Photo

UserModel = get_user_model()


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    imageUrl = serializers.CharField()

    class Meta:
        model = Photo
        fields = '__all__'
