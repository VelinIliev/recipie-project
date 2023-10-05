from django.urls import path, include

from server.api.users.views import UsersApiView, UserRecipiesApiView, UserEditApiView

urlpatterns = [
    path('', UsersApiView.as_view(), name='users list'),
    path('<int:pk>/', UserEditApiView.as_view(), name='user upload photo'),
    path('recipies/<int:user_pk>/', UserRecipiesApiView.as_view(), name='user recipies view'),
]
