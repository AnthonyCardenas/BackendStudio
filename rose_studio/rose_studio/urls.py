"""
URL configuration for rose_studio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# from gallery import views as gallery_views
# from reviews import views as reviews_views
# from packages import views as packages_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path('api/', include('gallery.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include("packages.urls")),
    path('api/', include("contact.urls")),
    
    # --- Catch-all for React ---
#     re_path(r"^(?:.*)/?$", TemplateView.as_view(template_name="index.html")),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [ #repath to index to find webpages
    re_path(r"^(?:.*)/?$", TemplateView.as_view(template_name="index.html")),
]