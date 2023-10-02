from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from server.user_app.api.views import registration_view, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login user'),
    path('register/', registration_view, name='register user'),
    path('logout/', logout_view, name='logout user'),
]
