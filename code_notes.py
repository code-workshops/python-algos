# JWT Flow
# 1. Client sends login request with username and password.
# 2. API validates credentials and creates a payload with user id.
# 3. API creates a refresh token for the client.
# 4. Refresh token is stored in the database along with user_id
# 5. Encrypt user data and create JWT
# 6. Return JWT and refresh token to the client.

    def validate(self, attrs):
        try:
            current_token = Token.objects.get(key=attrs.get('refresh_token'))
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Token does not exist.')
        else:
            exp_date = current_token.created + settings.JWT_REFRESH_EXP_DELTA
            user = current_token.user
            if exp_date < datetime.datetime.utcnow():
                current_token.delete()

        attrs['user'] = UserSerializer(user).data
        return attrs


# DRF JWT Request flow
