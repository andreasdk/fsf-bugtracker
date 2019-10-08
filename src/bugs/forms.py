from django import forms
from .models import Bug, BugComment

# ----- Bug Creation Form ----- #
class BugForm(forms.ModelForm):
    title = forms.CharField(
        min_length=10,
        max_length=60,
        widget=forms.TextInput(attrs={'placeholder': 'Bug Title'}),
        required=True
    )
    description = forms.CharField(
        min_length=20,
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Bug Description'}),
        required=True
    )

    class Meta:
        model = Bug
        fields = ('title', 'description')

class BugCommentForm(forms.ModelForm):
    comment = forms.CharField(
        min_length=20,
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Enter comment'}),
        required=True
    )

    class Meta:
        model = BugComment
        fields = ('comment',)

