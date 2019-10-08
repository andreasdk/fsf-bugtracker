from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from django.conf import settings
from .models import BugStatus, BugStatus
from .forms import BugForm

User = settings.AUTH_USER_MODEL


class TestBugForm(TestCase):
    def test_bug_report(self):
        form = BugForm(
            {'title':'New bug title', 
            'description': 'This is a new bug description'})
        self.assertTrue(form.is_valid())