from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.recipies.models import Comment

UserModel = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'recipie', 'comment_user']
