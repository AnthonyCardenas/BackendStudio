from django.db import models

from gallery.models import Photo

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=100)

    name = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    on_site_time = models.CharField(max_length=100)
    deliverable = models.CharField(max_length=200)
    raw = models.BooleanField(default=False) 

    vid_preview = models.BooleanField(default=False) 
    drone = models.BooleanField(default=False) 
    
    photo_preview = models.BooleanField(default=False)
    second_photographer = models.BooleanField(default=False) 

    category = models.CharField(max_length=100) #Ex. 
    level = models.CharField(max_length=100, blank=True) # Ex. Gold

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return self.title


class PricingGuide(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    packages = models.ManyToManyField( 
        Package, 
        blank=True,
        related_name="guides"
    )
    photos = models.ManyToManyField(
        Photo,
        blank=True,
        related_name="guides"
    )

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title
    

