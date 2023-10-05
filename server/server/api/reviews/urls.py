from django.urls import path

from server.api.reviews.views import ReviewsApiView, ReviewsApiRetrieveUpdateDestroy, RecipieReviewsApiView

urlpatterns = [
    path('', ReviewsApiView.as_view(), name='reviews view'),
    path('<int:pk>/', ReviewsApiRetrieveUpdateDestroy.as_view(), name='review view-update-delete'),
    path('recipie/<int:recipie_pk>/', RecipieReviewsApiView.as_view(), name='reviews recipie '),
]
