from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views, permissions
from rest_framework.exceptions import ValidationError

from server.api.permissions import ReviewUserOrReadOnly
from server.api.reviews.serializers import ReviewSerializer, CreateReviewSerializer
from server.recipies.models import Review

from django_filters.rest_framework import DjangoFilterBackend

UserModel = get_user_model()


class ReviewsApiView(rest_views.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by("-created")
    permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username', 'rating']


class ReviewsApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]


class RecipieReviewsApiView(rest_views.ListAPIView):
    serializer_class = ReviewSerializer
    # queryset = Review.objects.filter(active=True)

    def get_queryset(self):
        print("OK")
        recipie_pk = self.kwargs.get('recipie_pk')

        try:
            reviews = Review.objects.filter(recipie_id=recipie_pk, active=True)
        except Review.DoesNotExist:
            raise ValidationError("No recipie found.")

        return reviews

