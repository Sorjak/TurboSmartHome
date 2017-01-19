from django.apps import AppConfig
from allauth.account.signals import user_signed_up
# from allauth.socialaccount.signals import pre_social_login



class TurboSmartHomeConfig(AppConfig):
    name = 'turbosmarthome.main'
    verbose_name = "Main"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        # user_signed_up.connect(self.signedUpSignal)
        # pre_social_login.connect(self.socialLoginSignal)

    def signedUpSignal(self, request, user, **kwargs):
        from allauth.socialaccount.models import SocialAccount
        from turbosmarthome.main.models import Profile
        social_account = SocialAccount.objects.get(user=user.id)
        profile = Profile.objects.get(user=user.id)

        