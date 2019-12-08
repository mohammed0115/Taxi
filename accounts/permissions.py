


import uuid
from django.utils.translation import ugettext as _
from rest_framework import permissions, exceptions
from .auth.utils import get_api_key_header
from django.contrib.auth.models import User
from APIKEY.models import APIKey

class HasValidAPIKey(permissions.BasePermission):
    message = exceptions.ErrorDetail(_('You don\'t have permission to access this service. Please make sure you provided the correct API key.'), code="api_key_permission_denied")

    def has_permission(self, request, view):
        api_key_value = str(get_api_key_header(request), 'utf-8')

        if not api_key_value:
            msg = _('Invalid API-KEY header. No value provided.')
            raise exceptions.PermissionDenied(msg, code='api_key_not_provided')

        try:
            api_key = APIKey.objects.get(key=uuid.UUID(api_key_value))
            return api_key.active
        except APIKey.DoesNotExist:
            return False
        except ValueError:
            return False


class IsMerchantOrServiceCenterUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and \
            (request.user.user_type == User.USER_TYPE_MERCHANT
                or request.user.user_type == User.USER_TYPE_SERVICE_CENTER)

