from rest_framework import generics
from ..models import Client, Work, Artist
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, WorkSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def register_list(request):
    if request.method == 'GET':
        obj = User.objects.all()
        serializer = RegistrationSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def register_detail(request, pk):
    try:
        obj = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(obj)
        return Response(serializer.data)



class WorksListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['work_type']
    search_fields = ['work_type']


class ArtistListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['work_type']







