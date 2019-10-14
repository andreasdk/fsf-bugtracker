from django.test import TestCase, Client
from django.shortcuts import reverse, get_object_or_404
from django.conf import settings
from .forms import FeatureForm, FeatureCommentForm
from .models import Feature
from django.contrib.auth.models import User

#User = settings.AUTH_USER_MODEL

# Form Tests
class TestFeatureForm(TestCase):
    def test_feature_valid(self):
        form = FeatureForm(
            {'title':'New feature title', 
            'description': 'This is a new feature description'})
        self.assertTrue(form.is_valid())

    def test_feature_report_errors(self):
        form = FeatureForm({'title': 'New feature title', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

        form = FeatureForm({'title': '', 'description': 'This is a new feature description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

class TestFeatureComment(TestCase):
    def test_feature_comment_valid(self):
        form = FeatureCommentForm({
            'comment': 'This is a comment with enough characters'
        })
        self.assertTrue(form.is_valid())

    def test_feature_comment_invalid(self):
        form = FeatureCommentForm({
            'comment': 'Short comment'
        })
        self.assertFalse(form.is_valid())

# View Tests
class TestFeatureView(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_new_feature_view(self):
        response = self.client.get('/features/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/new.html')
    
    def test_view_all_features(self):
        response = self.client.get('/features/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/view_all.html')
    
    def test_view_single_feature(self):
        user = User.objects.get(username='testuser')
        feature = Feature(
            title='Feature test title', 
            description='This is a new feature description',
            author_id=user.id)
        feature.save()
        response = self.client.get('/features/{}'.format(feature.pk))
        self.assertEqual(response.status_code, 301)