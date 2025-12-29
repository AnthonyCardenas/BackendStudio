from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Package, PricingGuide
from .serializers import PackageSerializer, PricingGuideSerializer

# Create your views here.

@api_view(["GET"])
def pricing_guides(request):
    guides = PricingGuide.objects.all()
    serializer = PricingGuideSerializer(guides, many=True)
    return Response(serializer.data)
