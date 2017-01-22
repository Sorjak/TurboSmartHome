from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    nickname = models.CharField('Nickname', max_length=255, blank=True)
    phone_number = models.CharField('Phone Number', max_length=16, blank=True)

    def __str__(self):
        return self.nickname if self.nickname else self.user.username

    # Properties

    @property
    def avatar_url(self):
        social_account = SocialAccount.objects.get(user=self.user.id)
        return social_account.get_avatar_url()


    # Signals

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and not instance.is_superuser:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if not instance.is_superuser:
            instance.profile.save()