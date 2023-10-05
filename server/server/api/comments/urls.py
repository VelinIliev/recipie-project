from django.urls import path

from server.api.comments.views import CommentsApiView, CommentsReviewsApiView, CommentsApiRetrieveUpdateDestroy

urlpatterns = [
    path('', CommentsApiView.as_view(), name='comments view'),
    path('<int:pk>/', CommentsApiRetrieveUpdateDestroy.as_view(), name='comments view-update-delete'),
    path('recipie/<int:recipie_pk>/', CommentsReviewsApiView.as_view(), name='recipie comments'),
]
