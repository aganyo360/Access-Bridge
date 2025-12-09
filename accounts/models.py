from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    organization = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    # basic accessibility-focused fields
    is_service_provider = models.BooleanField(default=False)
    accessibility_contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
