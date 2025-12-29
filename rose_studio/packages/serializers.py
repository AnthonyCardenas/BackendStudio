from rest_framework import serializers
from .models import Package, PricingGuide
from gallery.models import Photo
from gallery.serializers import PhotoSerializer


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class PricingGuideSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = PricingGuide
        fields = ["id", "title", "category", "packages", "photos" ]

