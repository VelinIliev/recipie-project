from django.urls import path

from server.api.views import recipie_list, RecipiesApiView

urlpatterns = [
    path('', RecipiesApiView.as_view(), name='recipies list'),
    # path('<int:pk>', recipie_details, name='recipie details'),
]