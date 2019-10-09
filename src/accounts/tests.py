from django.test import TestCase
from django.shortcuts import reverse
from accounts.forms import (
    UserLoginForm, UserRegistrationForm,
    UserUpdateForm, ProfileUpdateForm)

# Account View Tests
class TestRegisterView(TestCase):
    def test_register_view(self):
        page = self.client.get('/account/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/register.html')

class TestLoginView(TestCase):
    def test_login_view(self):
        page = self.client.get('/account/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'accounts/login.html')


class TestLogoutView(TestCase):
    def test_logout_view(self):
        page = self.client.get("/account/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('index'))

class TestProfileView(TestCase):
    def test_profile_view(self):
        page = self.client.get("/account/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('profile'))
