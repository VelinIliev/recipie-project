from django.urls import path

from server.api.recipies.views import RecipiesApiView, RecipieApiView, RecipieCategoryApiView, ReviewsApiCreate, \
    CommentsApiCreate, PhotoUploadApi, RecipieCategoryApiAdd

urlpatterns = [
    path('', RecipiesApiView.as_view(), name='recipies list'),
    path('<int:pk>/', RecipieApiView.as_view(), name='recipie details'),
    path('<str:category>/', RecipieCategoryApiView.as_view(), name='recipies by category'),
    path('<int:recipie_pk>/review-create/', ReviewsApiCreate.as_view(), name='recipie review create'),
    path('<int:recipie_pk>/comment-create/', CommentsApiCreate.as_view(), name='recipie comment create'),
    path('<int:recipie_pk>/photo/', PhotoUploadApi.as_view(), name='recipie photo upload'),
    path('<int:recipie_pk>/category/<int:category_pk>/', RecipieCategoryApiAdd.as_view(), name='recipie category add'),
]