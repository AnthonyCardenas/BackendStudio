from rest_framework import routers
from .views import ReviewViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('reviews/', Review, name='reviews'),
# ]