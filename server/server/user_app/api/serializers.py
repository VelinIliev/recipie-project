from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords are not the same.'})

        if UserModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"error": "This email is already in use"})

        account = UserModel(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        account.set_password(password)
        account.save()

        return account
