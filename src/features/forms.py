from django import forms
from .models import Feature, FeatureComment

# ----- Feature Creation Form ----- #
class FeatureForm(forms.ModelForm):
    title = forms.CharField(
        min_length=10,
        max_length=60,
        widget=forms.TextInput(attrs={'placeholder': 'Feature Title'}),
        required=True
    )
    description = forms.CharField(
        min_length=20,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Feature Description'}),
        required=True
    )

    class Meta:
        model = Feature
        fields = ('title', 'description')

class FeatureCommentForm(forms.ModelForm):
    comment = forms.CharField(
        min_length=20,
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Enter comment'}),
        required=True
    )

    class Meta:
        model = FeatureComment
        fields = ('comment',)
