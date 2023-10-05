from django.urls import path

from server.api.categories.views import CategoriesApiView, CategoriesApiRetrieveUpdateDestroy

urlpatterns = [
    path('', CategoriesApiView.as_view(), name='categories view'),
    path('<int:pk>/', CategoriesApiRetrieveUpdateDestroy.as_view(), name='categories view-update-delete'),
]