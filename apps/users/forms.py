import logging

import requests
from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from apps.utils.timezones import get_timezones_display

from .helpers import validate_profile_picture
from .models import CustomUser


class TurnstileSignupForm(SignupForm):
    """
    Sign up form that includes a turnstile captcha.
    """

    turnstile_token = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_turnstile_token(self):
        if not settings.TURNSTILE_SECRET:
            logging.info("No turnstile secret found, not checking captcha")
            return

        turnstile_token = self.cleaned_data.get("turnstile_token", None)
        if not turnstile_token:
            raise forms.ValidationError("Missing captcha. Please try again.")

        turnstile_url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
        payload = {
            "secret": settings.TURNSTILE_SECRET,
            "response": turnstile_token,
        }
        try:
            response = requests.post(turnstile_url, data=payload, timeout=10).json()
            if not response["success"]:
                raise forms.ValidationError("Invalid captcha. Please try again.")
        except requests.Timeout:
            raise forms.ValidationError("Captcha verification timed out. Please try again.")

        return turnstile_token


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label=_("Email"), required=True)
    language = forms.ChoiceField(label=_("Language"))
    timezone = forms.ChoiceField(label=_("Time Zone"), required=False)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "language", "timezone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        timezone = self.fields.get("timezone")
        timezone.choices = get_timezones_display()
        if settings.USE_I18N and len(settings.LANGUAGES) > 1:
            language = self.fields.get("language")
            language.choices = settings.LANGUAGES
        else:
            self.fields.pop("language")


class UploadAvatarForm(forms.Form):
    avatar = forms.FileField(validators=[validate_profile_picture])
