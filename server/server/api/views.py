from rest_framework import generics as rest_views
from rest_framework.response import Response

from server.api.serializers import RecipiesSerializer, RecipieSerializer, ReviewSerializer, CreateReviewSerializer
from server.recipies.models import Recipie, Review


# @api_view(['GET', 'POST'])
# def recipie_list(request):
#     if request.method == 'GET':
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def recipie_details(request, pk):
#     try:
#         recipie = Recipie.objects.filter(pk=pk).get()
#     except Recipie.DoesNotExist:
#         return Response({'error': 'recipie not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ListRecipiesAV(APIView):
#
#     def get(self, request):
#         recipies = Recipie.objects.all()
#         serializer = TestSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TestSerializerOne(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class DetailsRecipieAV(APIView):
#
#     def get(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(recipie)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         serializer = TestSerializerOne(instance=recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         recipie = Recipie.objects.filter(pk=pk).get()
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class RecipiesApiView(rest_views.ListCreateAPIView):
    serializer_class = RecipiesSerializer
    queryset = Recipie.objects.all().order_by("-_created_at")

    def post(self, request, *args, **kwargs):
        serializer = RecipieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.list(request, *args, **kwargs)


class RecipieApiView(rest_views.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipieSerializer
    queryset = Recipie.objects.all()


class RecipieCategoryApiView(rest_views.ListAPIView):
    serializer_class = RecipiesSerializer
    lookup_url_kwarg = 'category'

    def get_queryset(self):
        category = self.kwargs.get(self.lookup_url_kwarg).title()
        queryset = Recipie.objects.filter(category__name=category)
        return queryset


class RecipieReviewApiView(rest_views.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        recipie_pk = self.kwargs['pk']
        return Review.objects.filter(recipie_id=recipie_pk)


class ReviewsApiView(rest_views.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by("-created")


class ReviewsApiCreate(rest_views.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer

    def perform_create(self, serializer):
        get_pk = self.kwargs.get('recipie_pk')
        recipie = Recipie.objects.filter(id=get_pk).get()
        serializer.save(recipie=recipie)


class ReviewsApiRetrieveUpdateDestroy(rest_views.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer
