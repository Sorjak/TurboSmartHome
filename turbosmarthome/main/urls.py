
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from turbosmarthome.main.views import *

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]