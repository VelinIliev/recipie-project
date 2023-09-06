from django.urls import path

from server.api.views import RecipiesApiView, RecipieApiView, recipie_list, recipie_details, ListRecipiesAV, \
    DetailsRecipieAV

urlpatterns = [
    path('recipies/test/', recipie_list, name='recipies list test'),
    path('recipies/test/<int:pk>/', recipie_details, name='recipies details test'),
    path('recipies/test2/', ListRecipiesAV.as_view(), name='recipies list test2'),
    path('recipies/test2/<int:pk>/', DetailsRecipieAV.as_view(), name='recipies details test2'),
    path('recipies/', RecipiesApiView.as_view(), name='recipies list'),
    path('recipies/<int:pk>/', RecipieApiView.as_view(), name='recipie details'),
]
