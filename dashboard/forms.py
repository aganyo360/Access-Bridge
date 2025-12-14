from django import forms
from organizations.models import Organization
from services.models import Service

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'city', 'address', 'latitude', 'longitude']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'organization', 'city', 'address', 'latitude', 'longitude', 'accessibility']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }
