from rest_framework import generics as rest_views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from server.api.serializers import RecipiesSerializer, RecipieSerializer, TestSerializer, TestSerializerOne
from server.recipies.models import Recipie


@api_view(['GET', 'POST'])
def recipie_list(request):
    if request.method == 'GET':
        recipies = Recipie.objects.all()
        serializer = TestSerializer(recipies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TestSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def recipie_details(request, pk):
    try:
        recipie = Recipie.objects.filter(pk=pk).get()
    except Recipie.DoesNotExist:
        return Response({'error': 'recipie not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TestSerializerOne(recipie)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TestSerializerOne(instance=recipie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        recipie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListRecipiesAV(APIView):

    def get(self, request):
        recipies = Recipie.objects.all()
        serializer = TestSerializer(recipies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DetailsRecipieAV(APIView):

    def get(self, request, pk):
        recipie = Recipie.objects.filter(pk=pk).get()
        serializer = TestSerializerOne(recipie)
        return Response(serializer.data)

    def put(self, request, pk):
        recipie = Recipie.objects.filter(pk=pk).get()
        serializer = TestSerializerOne(instance=recipie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        recipie = Recipie.objects.filter(pk=pk).get()
        recipie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipiesApiView(rest_views.ListAPIView):
    serializer_class = RecipiesSerializer

    def get_queryset(self):
        queryset = Recipie.objects.all()
        return queryset


class RecipieApiView(rest_views.RetrieveAPIView, rest_views.UpdateAPIView, rest_views.DestroyAPIView):
    serializer_class = RecipieSerializer
    lookup_url_kwarg = 'pk'
    queryset = Recipie.objects.all()


