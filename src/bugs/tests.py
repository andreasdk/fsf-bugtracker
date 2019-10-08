from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from django.conf import settings
from .forms import BugForm, BugCommentForm

User = settings.AUTH_USER_MODEL


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