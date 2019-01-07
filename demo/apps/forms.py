from django import forms
from django.contrib.auth.forms import AuthenticationForm as djAuthForm, UsernameField
from django.utils.translation import ugettext_lazy as _


class AuthenticationForm(djAuthForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, "placeholder": _("Username")}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": _("Password")}),
    )

    remember_me = forms.ChoiceField(
        label=_("Remember Me"),
        widget=forms.CheckboxInput(),
    )
