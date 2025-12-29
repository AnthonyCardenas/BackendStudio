from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import ScopedRateThrottle
# from ratelimit.decorators import ratelimit
from .serializers import ContactSerializer
# import os

# Create your views here.
class ContactView(APIView):
    # @ratelimit(key="ip", rate="3/m", block=True)
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "contact"

    def post(self, request):
        
        # Honeypot
        if request.data.get("company"):
            return Response(status=204) # discard data
        
        # CAPTCHA
        # token = request.data.get("captcha_token")
        # if not token:
        #     return Response(
        #         {"detail": "Captcha required"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )

        # result = verify_recaptcha(token, request.META.get("REMOTE_ADDR"))

        # if not result.get("success"):
        #     return Response(status=400)

        # if result.get("score", 0) < 0.5:
        #     return Response(
        #         {"detail": "Captcha score too low"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        
        # Success, regular save
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # triggers email via signal
            return Response({"message": "Submission received"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
