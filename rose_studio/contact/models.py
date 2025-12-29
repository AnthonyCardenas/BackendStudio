from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True) #change to Char field with 2000 max len
    company = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"