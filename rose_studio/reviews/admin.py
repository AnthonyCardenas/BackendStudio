from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'rating', 'description', 'source', 'category', 'created_at')

admin.site.register(Review, ReviewAdmin)