from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.00)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title