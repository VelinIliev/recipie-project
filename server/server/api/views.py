from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from rest_framework import generics as rest_views, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from server.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from server.api.serializers import RecipiesSerializer, RecipieSerializer, ReviewSerializer, CreateReviewSerializer, \
    CategorySerializer, CommentSerializer, PhotoSerializer, UserSerializer, EditExtendAppUserSerializer
from server.recipies.models import Recipie, Review, Category, Comment, Photo
from server.user_app.models import ExtendAppUser

UserModel = get_user_model()


# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# @api_view(['GET', 'POST'])
# def recipie_list(request):
#     if request.method == 'GET':
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def recipie_details(request, pk):
#     try:
#         recipie = Recipie.objects.filter(pk=pk).get()
#     except Recipie.DoesNotExist:
#         return Response({'error': 'recipie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ListRecipiesAV(APIView):
#
#     def get(self, request):
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class DetailsRecipieAV(APIView):
#
#     def get(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class RecipiesApiView(rest_views.ListCreateAPIView):
    serializer_class = RecipiesSerializer
    queryset = Recipie.objects.all().order_by("-_created_at")

    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # permission_classes = [CreateOrReadOnly]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = RecipieSerializer(data={**request.data, "user": user.pk})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        if isinstance(request.user, AnonymousUser):
            return Response({"error": "Not logged user"})
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class RecipieApiView(rest_views.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipieSerializer
    queryset = Recipie.objects.all()


class RecipieCategoryApiView(rest_views.ListAPIView):
    serializer_class = RecipiesSerializer
    lookup_url_kwarg = 'category'

    def get_queryset(self):
        category = self.kwargs.get(self.lookup_url_kwarg).title()
        queryset = Recipie.objects.filter(category__name=category)
        return queryset


class RecipieReviewApiView(rest_views.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        recipie_pk = self.kwargs['pk']
        return Review.objects.filter(recipie_id=recipie_pk)


class ReviewsApiView(rest_views.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by("-created")
    permission_classes = [permissions.IsAuthenticated]


class ReviewsApiCreate(rest_views.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        get_pk = self.kwargs.get('recipie_pk')

        try:
            recipie = Recipie.objects.filter(id=get_pk).get()
        except Recipie.DoesNotExist:
            raise ValidationError("No recipie found.")

        review_user = self.request.user
        review_queryset = Review.objects.filter(recipie=recipie, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You already reviewed this recipie.")

        reviews = Review.objects.filter(recipie=recipie)
        number_of_reviews = len(reviews) + 1
        current_rating_sum = sum([x.rating for x in reviews])

        new_rating = (current_rating_sum + serializer.validated_data['rating']) / number_of_reviews

        recipie.avg_rating = new_rating
        recipie.total_reviews = number_of_reviews
        recipie.save()

        serializer.save(recipie=recipie, review_user=review_user)


class ReviewsApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]


class RecipieReviewsApiView(rest_views.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.filter(active=True)

    def get_queryset(self):
        recipie_pk = self.kwargs.get('recipie_pk')
        return Review.objects.filter(recipie_id=recipie_pk, active=True)


class CategoriesApiView(rest_views.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminOrReadOnly]


class CategoriesApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]


class CommentsApiCreate(rest_views.CreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        get_pk = self.kwargs.get('recipie_pk')
        recipie = Recipie.objects.filter(id=get_pk).get()
        comment_user = self.request.user
        serializer.save(recipie=recipie, comment_user=comment_user)


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


class UserRecipiesApiView(rest_views.ListAPIView):
    serializer_class = RecipiesSerializer

    # queryset = Recipie.objects.all()

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        return Recipie.objects.filter(user_id=user_pk)


class PhotoUploadApi(rest_views.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        recipie_pk = self.kwargs.get('recipie_pk')
        file = request.data['file']
        image = Photo.objects.create(imageUrl=file, recipie_id=recipie_pk)
        return Response({'message': "Uploaded"})


class UsersApiView(rest_views.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserEditApiView(rest_views.UpdateAPIView):
    queryset = ExtendAppUser.objects.all()
    serializer_class = EditExtendAppUserSerializer

    def put(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('pk')
        user = ExtendAppUser.objects.filter(user_id=user_pk).get()
        file = request.data['file']
        extension = str(file).split(".")[-1]
        user.imageUrl.save(f'{request.user.username}-photo.{extension}', file)
        user.save()
        return Response({'message': "Uploaded"})
