# views go in here
from __future__ import absolute_import, unicode_literals

from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

from turbosmarthome.main.forms import ProfileEditForm
from turbosmarthome.main.models import *

class HomePageView(TemplateView):
    template_name = "main/home.html"

class UserInfoView(UpdateView):
    template_name = "main/profile_edit.html"
    form_class = ProfileEditForm
    success_url = "/accounts/profile"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/accounts/login')

        return super(UserInfoView, self).dispatch(request, *args, **kwargs)

class UserProfileView(TemplateView):
    template_name = "account/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/accounts/login')
        else: 
            p = Profile.objects.get(user=request.user)
            if not p.active:
                return redirect('/accounts/update')

        return super(UserProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)

        try:
            context['profile'] = Profile.objects.select_related('user').get(user=self.request.user)
        except Exception as e:
            print(e)

        return context

        
