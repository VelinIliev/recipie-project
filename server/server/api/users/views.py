from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views
from rest_framework.response import Response

from server.api.recipies.serializers import RecipiesSerializer
from server.api.users.serializer import UserSerializer, EditExtendAppUserSerializer
from server.recipies.models import Recipie
from server.user_app.models import ExtendAppUser

UserModel = get_user_model()


class UserRecipiesApiView(rest_views.ListAPIView):
    serializer_class = RecipiesSerializer

    # queryset = Recipie.objects.all()

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        return Recipie.objects.filter(user_id=user_pk)


class UsersApiView(rest_views.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserEditApiView(rest_views.UpdateAPIView):
    queryset = ExtendAppUser.objects.all()
    serializer_class = EditExtendAppUserSerializer

    def put(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('pk')
        user = ExtendAppUser.objects.filter(user_id=user_pk).get()
        print(request.data)
        file = request.data['file']
        extension = str(file).split(".")[-1]
        user.imageUrl.save(f'{request.user.username}-photo.{extension}', file)
        user.save()
        return Response({'message': "Uploaded"})
