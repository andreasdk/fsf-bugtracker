from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from features.models import Feature


# Cart View Tests
class TestRegisterView(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_cart_view(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart/cart.html')
        
        page = self.client.get('/carts/')
        self.assertEqual(page.status_code, 404)
        self.assertTemplateNotUsed(page, 'cart/cart.html')

