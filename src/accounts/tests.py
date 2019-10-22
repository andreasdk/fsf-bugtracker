from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.forms import (
    UserLoginForm, UserRegistrationForm,
    UserUpdateForm, ProfileUpdateForm)

# Account Form Tests
class TestAccountLoginForm(TestCase):
    def test_login_form_valid(self):
        form = UserLoginForm(
            {"username": "TestUsername", 
            "password": "TestPassword"
            })
        self.assertTrue(form.is_valid())
    
    def test_login_form_invalid(self):
        form = UserLoginForm(
            {'username': '', 
            'password': ''
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': [u'This field is required.'],
                                       'password': [u'This field is required.']})


def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

class TestAccountsRegistrationForm(TestCase):
    def test_registration_valid(self):
        form = UserRegistrationForm({'username':"testuser1",
                                     "password1": "test_password",
                                     "password2": "test_password",
                                     "email": "test@example.com"})
        self.assertTrue(form.is_valid())
    
    def test_registration_form_invalid(self):
        form = UserRegistrationForm(
            {'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], [u"This field is required."])


    def test_username_already_exists(self):
        setUp(self)
        form = UserRegistrationForm({'username':"testuser",
                                     "password1": "12345",
                                     "password2": "12345",
                                     "email": "test@example.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],
                                    [u'A user with that username already exists.'])
    
    def test_passwords_do_not_match(self):
        form = UserRegistrationForm({'username': 'tesuser',
                                     'password1': 'test_pass1',
                                     'password2': 'test_pass2',
                                     "email": "test@example.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])

class TestUserUpdateForm(TestCase):
    def test_update_user_email(self):
        form = UserUpdateForm({"email": "new@example.com"})
        form.save()
        self.assertTrue(form.is_valid())

class TestProfileUpdateForm(TestCase):
    def test_update_profile_image(self):
        newImage = ProfileUpdateForm
        newImage.image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg")
        self.client.post(reverse("profile"), {"newImage": newImage})
        self.assertIsNotNone(ProfileUpdateForm)

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
