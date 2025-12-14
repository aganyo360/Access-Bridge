from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class DashboardAccessTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='normal', password='pass123')
        self.staff = User.objects.create_user(username='staff', password='pass123')
        self.staff.is_staff = True
        self.staff.save()

    def test_non_staff_cannot_access(self):
        self.client.login(username='normal', password='pass123')
        resp = self.client.get(reverse('dashboard:index'))
        # should be 302 redirect to login because of user_passes_test
        self.assertIn(resp.status_code, (302, 403))

    def test_staff_can_access(self):
        self.client.login(username='staff', password='pass123')
        resp = self.client.get(reverse('dashboard:index'))
        self.assertEqual(resp.status_code, 200)
