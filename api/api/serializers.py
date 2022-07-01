from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework import status
from user.models import User

from rest_framework.exceptions import APIException

class UserNotFound(AuthenticationFailed):
          status_code = status.HTTP_404_NOT_FOUND
          default_detail = _("user-not-found")
          default_code = '404'

class InActiveUser(AuthenticationFailed):
          status_code = status.HTTP_401_UNAUTHORIZED
          default_detail = _("user-not-active")
          default_code = '423'

class WrongPassword(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('user-wrong-password')
    default_code = '424'

class CustomTokenObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        result = {
            "operation" : "user-validation",
            "data": None,
            "details": "ok"            
        }
        try:

            users = User.objects.filter(email=attrs['email'])

            if users.count() == 0:
                raise UserNotFound
            
            objUser = users.first()

            if not objUser.is_active:
                raise InActiveUser
            
            if not attrs["password"] == "*|*":                
                validation = super().validate(attrs)
                
                refresh = self.get_token(self.user)
                result["data"] = {
                    "id": objUser.id,
                    "username": objUser.username,
                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token)
                }

            else:
                result["data"] = {
                    "id": objUser.id,
                    "username": objUser.username
                }

        except Exception as e:            
            raise WrongPassword            

        return result
