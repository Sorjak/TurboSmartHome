# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.auth.models import User

from turbosmarthome.main.models import Profile


class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)
    class Meta:
        model = Profile
        fields = ['nickname', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        self.provided_email = None

        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control form-control-danger'

            

    def clean(self):
        cleaned_data = super(ProfileEditForm, self).clean()
        self.provided_email = cleaned_data['email']

        return cleaned_data

    def save(self, commit=True, *args, **kwargs):
        instance = super(ProfileEditForm, self).save(commit=False, *args, **kwargs)

        try:
            u = User.objects.get(id=instance.user.id)
            u.email = self.provided_email
            u.save()
        except Exception as e:
            print(e)

        if commit:
            instance.save()

        return instance