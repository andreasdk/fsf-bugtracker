from django.contrib import admin
from .models import Bug, BugComment

# Register your models here.
admin.site.register(Bug)
admin.site.register(BugComment)