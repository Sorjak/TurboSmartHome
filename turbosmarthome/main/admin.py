# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'active', 'nickname', 'phone_number')
    list_filter = ('user', 'active')
admin.site.register(Profile, ProfileAdmin)
