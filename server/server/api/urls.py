from django.urls import path

from server.api.views import RecipiesApiView, RecipieApiView, RecipieCategoryApiView, \
    RecipieReviewApiView, ReviewsApiView, ReviewsApiCreate, ReviewsApiRetrieveUpdateDestroy

urlpatterns = [
    path('recipies/', RecipiesApiView.as_view(), name='recipies list'),
    path('recipies/<int:pk>/', RecipieApiView.as_view(), name='recipie details'),

    path('recipies/<str:category>/', RecipieCategoryApiView.as_view(), name='recipie by category'),

    path('recipies/<int:pk>/review/', RecipieReviewApiView.as_view(), name='recipie reviews'),
    path('recipies/<int:recipie_pk>/review-create/', ReviewsApiCreate.as_view(), name='review create'),

    path('reviews/', ReviewsApiView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewsApiRetrieveUpdateDestroy.as_view(), name='review view-update-delete'),

]
