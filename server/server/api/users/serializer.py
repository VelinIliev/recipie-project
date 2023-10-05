from django.contrib.auth import get_user_model
from rest_framework import serializers

from server.user_app.models import ExtendAppUser

UserModel = get_user_model()


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
