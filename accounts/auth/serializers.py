
from django.utils.translation import ugettext as _

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from .utils import generate_jwt_token_payload, encode_jwt_token_payload

class BaseObtainTokenSerializer(JSONWebTokenSerializer):
    """
    Base serializer allows you to customize username field and the authenticate function
    """
    user_model_username_field = None

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = self.authenticate(attrs.get(self.username_field), attrs.get('password'))

            if user:
                if not user.is_active:
                    msg = _('User account is not active.')
                    raise serializers.ValidationError(msg, code="inactive_user")

                payload = self.get_payload(user)

                return {
                    'token': self.encode_payload(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='invalid_credentials')
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

    def get_payload(self, user):
        return generate_jwt_token_payload(user, self.user_model_username_field)

    def encode_payload(self, payload):
        return encode_jwt_token_payload(payload)

    def authenticate(self, username, password):
        raise NotImplementedError("authenticate is not implemented")
