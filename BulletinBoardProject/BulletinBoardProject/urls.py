from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('announcements/', include('announcements.urls')),
    path('', include(accounts_urls)),
]
