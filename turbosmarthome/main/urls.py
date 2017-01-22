
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from turbosmarthome.main.views import *
from turbosmarthome.main.api import *

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^api/toggle_lights/$', toggle_lights, name='toggle_lights'),
]