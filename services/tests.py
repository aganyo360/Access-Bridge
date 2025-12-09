from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from organizations.models import Organization
from .models import Service
from rest_framework import status

User = get_user_model()


class ServiceTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="serviceuser",
            password="StrongPass123"
        )
        self.org = Organization.objects.create(
            name="Org 1",
            created_by=self.user
        )

    def test_list_services_public(self):
        url = reverse('service-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_service_requires_auth(self):
        url = reverse('service-list')
        data = {
            "name": "Test Service",
            "description": "Test desc",
            "city": "Nairobi",
            "latitude": -1.29,
            "longitude": 36.82,
            "organization": self.org.id,
            "accessibility": "wheelchair_accessible"
        }

        # 1. Not logged in → must be 401
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # 2. Authenticate properly (DRF way)
        self.client.force_authenticate(user=self.user)

        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)


class ServiceFilterTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="pass123"
        )

        self.org = Organization.objects.create(
            name="Test Org",
            created_by=self.user
        )

        Service.objects.create(
            organization=self.org,
            name="Sign Language Center",
            description="For deaf persons",
            city="Nairobi",
            latitude=-1.28,
            longitude=36.82,
            accessibility="sign_language_support",
            created_by=self.user,
        )

        Service.objects.create(
            organization=self.org,
            name="Wheelchair Clinic",
            description="Physical disability support",
            city="Kisumu",
            latitude=-0.1,
            longitude=34.75,
            accessibility="wheelchair_accessible",
            created_by=self.user,
        )

    def test_filter_by_city(self):
        url = "/api/services/?city=Nairobi"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.json()), 1)
        self.assertEqual(resp.json()[0]["city"], "Nairobi")

    def test_filter_by_accessibility(self):
        url = "/api/services/?accessibility=wheel"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.json()), 1)
        self.assertIn("wheelchair", resp.json()[0]["accessibility"])
