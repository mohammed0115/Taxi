from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from accounts.models import user as User


class AccessTokenAuthentication(JSONWebTokenAuthentication):
    """
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string specified in the setting
    `JWT_AUTH_HEADER_PREFIX`. For example:

        Authorization: access_token eyJhbGciOiAiSFMyNTYiLCAidHlwIj
    In order to not expose how the token works in our system, we return AnonymousUser when credentials are invalid.
    The API user will get an permission denied error instead of detailed AuthenticationFailed error.
    """
    def authenticate(self, request):
        access_token = self.get_jwt_value(request)
        if access_token is None:
            return None

        if self.is_blacklisted(access_token):
            return (AnonymousUser(), None)
        try:
            return super(AccessTokenAuthentication, self).authenticate(request)
        except exceptions.AuthenticationFailed:
            return (AnonymousUser(), None)
        except User.DoesNotExist:
            # To handle the case when user_id inside the token doesn't exist.
            # This may happen when people try to attack the site.
            return (AnonymousUser(), None)

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's username.
        """
        username = payload["username"]

        if not username:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = self.get_user_by_username(username)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user

    def get_user_by_username(self, username):
        return User.objects.get_by_natural_key(username)

    def is_blacklisted(self, token):
        """
        Check whether a token is blacklisted
        Override this function to handle it in a different way
        """
        return False




def validate_password(password, user=None, password_validators=None):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise Django rest framework ValidationError with all error messages.

    """
    errors = []
    if password_validators is None:
        password_validators = password_validation.get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except DjangoValidationError as dex:
            message = dex.message
            if dex.params:
                message = message % dex.params
            errors += exceptions.ValidationError(message, code=dex.code).detail
        except exceptions.ValidationError as ex:
            errors += ex.detail
    if errors:
        raise exceptions.ValidationError(errors)

