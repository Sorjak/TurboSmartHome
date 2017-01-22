# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.auth.models import User

from turbosmarthome.main.models import Profile


class ProfileEditForm(forms.ModelForm):
    # email = forms.EmailField(label="Email", required=True)
    class Meta:
        model = Profile
        fields = ['nickname', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control form-control-danger'

    def save(self, commit=True, *args, **kwargs):
        instance = super(ProfileEditForm, self).save(commit=False, *args, **kwargs)
        instance.active = True

        if commit:
            instance.save()

        return instance