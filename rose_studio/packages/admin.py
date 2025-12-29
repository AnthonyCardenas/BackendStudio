from django.contrib import admin
from .models import Package, PricingGuide

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'on_site_time',  'deliverable', 'raw', 'vid_preview', 'drone', 'photo_preview', 'second_photographer', 'category', 'level')
    ordering = ('price', )

class PricingGuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', )

admin.site.register(Package, PackageAdmin)
admin.site.register(PricingGuide, PricingGuideAdmin)
