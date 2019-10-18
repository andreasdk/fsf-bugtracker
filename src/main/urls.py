from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import urls as account_urls
from bugs import urls as bug_urls
from features import urls as feature_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls

from .views import (
    index
)

urlpatterns = [
    path('', index, name="index"),
    path('account/', include(account_urls)),
    path('bugs/', include(bug_urls)),
    path('features/', include(feature_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', index, name="index"),
        path('account/', include(account_urls)),
        path('bugs/', include(bug_urls)),
        path('features/', include(feature_urls)),
        path('cart/', include(cart_urls)),
        path('checkout/', include(checkout_urls)),
        path('admin/', admin.site.urls),
    ]