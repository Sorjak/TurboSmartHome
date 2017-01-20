from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from django.views import defaults as default_views
from django.views.generic.base import TemplateView

from turbosmarthome.main.views import UserProfileView, UserInfoView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', UserProfileView.as_view(), name='account_profile' ),
    url(r'^accounts/update/', UserInfoView.as_view(), name='account_update' ),

    url(r'^', include('turbosmarthome.main.urls')),

    url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
    url(r'^500/$', default_views.server_error),
]
