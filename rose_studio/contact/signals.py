# contact/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

# import os

@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    if not created:
        return

    subject = f"New Contact Form Submission: {instance.subject or 'No Subject'}"
    message = f"""
Name: {instance.name}
Email: {instance.email}

Message:
{instance.message}
    """

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_TO_EMAIL],# where you want to receive it
        # ["your_email@gmail.com"],  
        fail_silently=False,
    )