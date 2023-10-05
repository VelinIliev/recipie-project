from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views

from server.api.comments.serializers import CommentSerializer
from server.api.permissions import AdminOrReadOnly
from server.recipies.models import Comment

UserModel = get_user_model()


class CommentsApiView(rest_views.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsReviewsApiView(rest_views.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        recipie_pk = self.kwargs.get('recipie_pk')
        return Comment.objects.filter(recipie_id=recipie_pk)


class CommentsApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AdminOrReadOnly]
