from django.shortcuts import render
from rest_framework import viewsets
from .models import Photo
from .serializers import PhotoSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-created_at')
    serializer_class = PhotoSerializer

# GET request handler
@api_view(['GET'])
@permission_classes([AllowAny])
def get_items(request):
    data = Photo.objects.all()
    serializer = PhotoSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)