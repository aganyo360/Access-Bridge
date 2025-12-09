from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Organization

User = get_user_model()

class OrganizationTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="orguser", password="StrongPass123"
        )

    def test_list_organizations_public(self):
        url = reverse("org-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_organization_requires_auth(self):
        url = reverse("org-list")
        data = {
            "name": "Test Org",
            "description": "Desc",
            "city": "Nairobi",
            "address": "123 Street"
        }

        # not logged in
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # login
        self.client.login(username="orguser", password="StrongPass123")
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organization.objects.count(), 1)
