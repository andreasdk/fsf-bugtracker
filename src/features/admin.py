from django.contrib import admin
from .models import Feature, FeatureComment, FeatureVotes

# Register your models here.
admin.site.register(Feature)
admin.site.register(FeatureComment)
admin.site.register(FeatureVotes)