from django.urls import path

from server.api.views import RecipiesApiView, RecipieApiView, recipie_list, recipie_details, ListRecipiesAV, \
    DetailsRecipieAV, RecipieCategoryApiView, RecipieReviewApiView, ReviewsApiView, RecipieApiDelete, RecipieApiUpdate, \
    ReviewsApiUpdate, ReviewsApiCreate, ReviewsApiDelete

urlpatterns = [
    path('recipies/test/', recipie_list, name='recipies list test'),
    path('recipies/test/<int:pk>/', recipie_details, name='recipies details test'),
    path('recipies/test2/', ListRecipiesAV.as_view(), name='recipies list test2'),
    path('recipies/test2/<int:pk>/', DetailsRecipieAV.as_view(), name='recipies details test2'),

    path('recipies/', RecipiesApiView.as_view(), name='recipies list'),
    path('recipies/<int:pk>/', RecipieApiView.as_view(), name='recipie details'),
    path('recipies/<int:pk>/delete/', RecipieApiDelete.as_view(), name='recipie delete'),
    path('recipies/<int:pk>/update/', RecipieApiUpdate.as_view(), name='recipie update'),

    path('recipies/<str:category>/', RecipieCategoryApiView.as_view(), name='recipie by category'),

    path('recipies/<int:pk>/review/', RecipieReviewApiView.as_view(), name='recipie reviews'),

    path('reviews/', ReviewsApiView.as_view(), name='recipie reviews'),
    path('reviews/<int:recipie_pk>/create/', ReviewsApiCreate.as_view(), name='review create'),
    path('reviews/<int:pk>/update/', ReviewsApiUpdate.as_view(), name='review update'),
    path('reviews/<int:pk>/delete/', ReviewsApiDelete.as_view(), name='review delete'),
]
