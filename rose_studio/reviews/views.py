from django.shortcuts import render
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer


# GET request handler
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_items(request):
#     data = Review.objects.all()
#     serializer = ReviewSerializer(data, context={'request': request}, many=True)
#     return Response(serializer.data)
