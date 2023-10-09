from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import generics as rest_views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from server.api.comments.serializers import CommentSerializer
from server.api.pagination import RecipiesPagination
from server.api.photos.serializers import PhotoSerializer
from server.api.recipies.serializers import RecipiesSerializer, RecipieSerializer
from server.api.reviews.serializers import ReviewSerializer, CreateReviewSerializer
from server.recipies.models import Recipie, Review, Comment, Photo, Category

UserModel = get_user_model()


class RecipiesApiView(rest_views.ListCreateAPIView):
    serializer_class = RecipiesSerializer
    # queryset = Recipie.objects.all().order_by("-_created_at")
    pagination_class = RecipiesPagination

    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # permission_classes = [CreateOrReadOnly]

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        order = self.request.query_params.get('order', None)
        queryset = Recipie.objects.all().order_by('-_created_at')

        if order:
            order = order.split(',')
            queryset = queryset.order_by(*[x for x in order])

        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__name__iexact=category)

        return queryset

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


class CommentsApiCreate(rest_views.CreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        get_pk = self.kwargs.get('recipie_pk')
        recipie = Recipie.objects.filter(id=get_pk).get()
        comment_user = self.request.user
        serializer.save(recipie=recipie, comment_user=comment_user)


class PhotoUploadApi(rest_views.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        recipie_pk = self.kwargs.get('recipie_pk')
        file = request.data['file']
        image = Photo.objects.create(imageUrl=file, recipie_id=recipie_pk)
        return Response({'message': "Uploaded"})


class RecipieCategoryApiAdd(rest_views.UpdateAPIView):
    serializer_class = RecipiesSerializer
    queryset = Recipie.objects.all()

    def patch(self, request, *args, **kwargs):
        get_pk = self.kwargs.get('recipie_pk')
        category_pk = self.kwargs.get('category_pk')

        try:
            recipie = Recipie.objects.filter(id=get_pk).get()
        except Recipie.DoesNotExist:
            raise ValidationError("No recipie found")

        try:
            category = Category.objects.filter(id=category_pk).get()
        except Category.DoesNotExist:
            raise ValidationError("No category found")

        recipie.category.add(category)
        return Response(status=201)
