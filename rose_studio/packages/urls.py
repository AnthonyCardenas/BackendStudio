from django.urls import path
from .views import pricing_guides

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'packages', PackageViewSet)

urlpatterns = [
    path("pricing-guides/", pricing_guides, name="pricing-guides")
]