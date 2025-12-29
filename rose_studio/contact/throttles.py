# contact/throttles.py
from rest_framework.throttling import SimpleRateThrottle
# from rest_framework.throttling import ScopedRateThrottle

class ContactThrottle(SimpleRateThrottle):
    scope = "contact"

    def get_cache_key(self, request, view):
        return self.get_ident(request)