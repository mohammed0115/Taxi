import uuid
from calendar import timegm
from datetime import datetime
from rest_framework_jwt.settings import api_settings as jwt_settings
from rest_framework_jwt.serializers import jwt_encode_handler
from django.utils.six import text_type
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.authentication import get_authorization_header

def generate_jwt_token_payload(user, username_field):
    username = getattr(user, username_field)

    payload = {
        'user_id': user.pk,
        'username': username,
        'exp': datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if jwt_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if jwt_settings.JWT_AUDIENCE is not None:
        payload['aud'] = jwt_settings.JWT_AUDIENCE

    if jwt_settings.JWT_ISSUER is not None:
        payload['iss'] = jwt_settings.JWT_ISSUER

    return payload

def encode_jwt_token_payload(payload):
    return jwt_encode_handler(payload)

def get_api_key_header(request):
    """
    Return request's 'API-KEY:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    api_key = request.META.get('HTTP_API_KEY', b'')
    if isinstance(api_key, text_type):
        # Work around django test client oddness
        api_key = api_key.encode(HTTP_HEADER_ENCODING)
    return api_key

def get_access_token(request):
    auth = get_authorization_header(request).split()
    if len(auth) is 2:
        return auth[1]
    else:
        return None
