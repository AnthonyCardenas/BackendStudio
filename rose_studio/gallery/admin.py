from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'image', 'category', 'tags', 'created_at')

admin.site.register(Photo, PhotoAdmin)