from django.db import models
from django.conf import settings
from organizations.models import Organization

class Service(models.Model):
    ACCESSIBILITY_CHOICES = [
        ('wheelchair', 'Wheelchair Accessible'),
        ('hearing', 'Hearing Support'),
        ('vision', 'Vision Support'),
        ('all', 'All Access'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='services')
    city = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    accessibility = models.CharField(max_length=20, choices=ACCESSIBILITY_CHOICES, default='all')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='services_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
