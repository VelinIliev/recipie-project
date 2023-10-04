from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import serializers

from server.recipies.models import Recipie, Category, Photo, Review, Comment
from server.user_app.models import ExtendAppUser

UserModel = get_user_model()


def description_validator(value):
    if len(value) < 2:
        raise serializers.ValidationError('Description is too short')


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    imageUrl = serializers.CharField()

    class Meta:
        model = Photo
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'description', 'recipie_id', 'review_user']


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


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()


class TestSerializerOne(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(validators=[description_validator, ])
    ingredients = serializers.CharField()
    preparation = serializers.CharField()
    preparation_time = serializers.IntegerField()
    cooking_time = serializers.IntegerField()
    portions = serializers.IntegerField()

    def create(self, validated_data):
        return Recipie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.preparation = validated_data.get('preparation', instance.preparation)
        instance.preparation_time = validated_data.get('preparation_time', instance.preparation_time)
        instance.cooking_time = validated_data.get('cooking_time', instance.cooking_time)
        instance.portions = validated_data.get('portions', instance.portions)
        instance.save()
        return instance

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


class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'recipie', 'comment_user']


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'gender', 'photo']

    def get_gender(self, object):
        extra_user = ExtendAppUser.objects.filter(user_id=object).get()
        return extra_user.gender

    def get_photo(self, object):
        extra_user = ExtendAppUser.objects.filter(user_id=object).get()
        if extra_user.imageUrl:
            return str(extra_user.imageUrl)
        else:
            return None


class EditExtendAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendAppUser
        fields = '__all__'
