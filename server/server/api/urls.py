from django.urls import path, include

urlpatterns = [
    path('recipies/', include('server.api.recipies.urls')),
    path('categories/', include('server.api.categories.urls')),
    path('reviews/', include('server.api.reviews.urls')),
    path('comments/', include('server.api.comments.urls')),
    path('users/', include('server.api.users.urls')),

]
