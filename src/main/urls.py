from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from accounts import urls as account_urls
from bugs import urls as bug_urls
from features import urls as feature_urls


from .views import (
    index
)

urlpatterns = [
    path('', index, name="index"),
    path('account/', include(account_urls)),
    path('bugs/', include(bug_urls)),
    path('features/', include(feature_urls)),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )