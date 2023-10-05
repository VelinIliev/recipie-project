from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.recipies.models import Review

UserModel = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'description', 'recipie_id', 'review_user']
