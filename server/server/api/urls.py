from django.urls import path

from server.api.views import RecipiesApiView, RecipieApiView, RecipieCategoryApiView, \
    ReviewsApiView, ReviewsApiCreate, ReviewsApiRetrieveUpdateDestroy, RecipieReviewsApiView, \
    CategoriesApiView, CategoriesApiRetrieveUpdateDestroy, CommentsApiCreate, CommentsApiView, CommentsReviewsApiView, \
    CommentsApiRetrieveUpdateDestroy, UserRecipiesApiView, PhotoUploadApi, UsersApiView, UserEditApiView

urlpatterns = [
    path('recipies/', RecipiesApiView.as_view(), name='recipies list'),
    path('recipies/<int:pk>/', RecipieApiView.as_view(), name='recipie details'),
    path('recipies/<str:category>/', RecipieCategoryApiView.as_view(), name='recipie by category'),
    path('recipies/<int:recipie_pk>/review-create/', ReviewsApiCreate.as_view(), name='recipie review create'),
    path('recipies/<int:recipie_pk>/comment-create/', CommentsApiCreate.as_view(), name='recipie comment create'),
    path('recipies/<int:recipie_pk>/photo/', PhotoUploadApi.as_view(), name='photo upload'),


    path('categories/', CategoriesApiView.as_view(), name='categories view'),
    path('categories/<int:pk>/', CategoriesApiRetrieveUpdateDestroy.as_view(), name='category view-update-delete'),

    path('reviews/', ReviewsApiView.as_view(), name='reviews view'),
    path('<int:recipie_pk>/reviews/', RecipieReviewsApiView.as_view(), name='recipie reviews'),
    path('reviews/<int:pk>/', ReviewsApiRetrieveUpdateDestroy.as_view(), name='review view-update-delete'),

    path('comments/', CommentsApiView.as_view(), name='comments view'),
    path('<int:recipie_pk>/comments/', CommentsReviewsApiView.as_view(), name='recipie comments'),
    path('comments/<int:pk>/', CommentsApiRetrieveUpdateDestroy.as_view(), name='comments view-update-delete'),

    path('user/recipies/<int:user_pk>/', UserRecipiesApiView.as_view(), name='user recipies view'),
    path('users/', UsersApiView.as_view(), name='user list'),
    path('user/<int:pk>/', UserEditApiView.as_view(), name='user edit')
]
