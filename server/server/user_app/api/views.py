from rest_framework import decorators, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from server.user_app.api.serializers import RegistrationSerializer


@decorators.api_view(["POST", ])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key

            data['response'] = 'Registration successful'
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)


@decorators.api_view(["POST", ])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

