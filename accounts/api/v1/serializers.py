from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _






class RgisterApiSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password','password_confirm']

        def validate(self,attrs):
            if attrs.get('password_confirm') != attrs.get("password"):
                raise serializers.ValidationError({"detail": "password dosnt match please try it"})

            try:
                validate_password(attrs.get("password"))
            except exceptions.ValidationError as e:
                raise serializers.ValidationError({"password": list(e.messages)})
            return super().validate(attrs)
        



class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
