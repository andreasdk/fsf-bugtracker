from django.test import TestCase, Client
from django.shortcuts import reverse, get_object_or_404
from django.conf import settings
from .forms import BugForm, BugCommentForm
from .views import new_bug
from django.contrib.auth.models import User

#User = settings.AUTH_USER_MODEL

# Form Tests
class TestBugForm(TestCase):
    def test_bug_valid(self):
        form = BugForm(
            {'title':'New bug title', 
            'description': 'This is a new bug description'})
        self.assertTrue(form.is_valid())

    def test_bug_report_errors(self):
        form = BugForm({'title': 'New bug title', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

        form = BugForm({'title': '', 'description': 'This is a new bug description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

class TestBugComment(TestCase):
    def test_bug_comment_valid(self):
        form = BugCommentForm({
            'comment': 'This is a comment with enough characters'
        })
        self.assertTrue(form.is_valid())

    def test_bug_comment_invalid(self):
        form = BugCommentForm({
            'comment': 'Short comment'
        })
        self.assertFalse(form.is_valid())

# View Tests
class TestBugView(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_new_bug_view(self):
        response = self.client.get('/bugs/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs/new.html')