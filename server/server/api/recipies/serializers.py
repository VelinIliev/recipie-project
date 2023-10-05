from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import serializers

from server.api.categories.serializers import CategorySerializer
from server.api.photos.serializers import PhotoSerializer
from server.recipies.models import Recipie

UserModel = get_user_model()


class RecipiesSerializer(serializers.ModelSerializer):
    BASE_URL = 'http://127.0.0.1:8000'
    category = CategorySerializer(many=True, read_only=True)
    link = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Recipie
        fields = ('id', 'title', 'description', 'category', 'link', 'photo', 'user')

    def get_link(self, recipie):
        relative_url = reverse('recipie details', args=[recipie.id])
        absolute_url = f'{self.BASE_URL}{relative_url}'
        return absolute_url

    def get_photo(self, object):
        photos = object.photos.first()
        if photos:
            serializer = PhotoSerializer(photos)
            return serializer.data
        else:
            return []


class RecipieSerializer(serializers.ModelSerializer):
    total_time = serializers.SerializerMethodField()
    category = CategorySerializer(many=True, read_only=True)
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Recipie
        fields = '__all__'

    def get_total_time(self, object):
        total = (int(object.preparation_time) if object.preparation_time else 0) \
                + (int(object.cooking_time if object.cooking_time else 0))
        return total

    def get_photos(self, object):
        # recipie = Recipie.objects.filter(id=15).get()
        photos = object.photos
        serializer = PhotoSerializer(photos, many=True)
        return serializer.data

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and description can not be the same.')
        else:
            return data

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Title is too short')
        elif len(value) > 150:
            raise serializers.ValidationError('Title is too long')
        else:
            return value
