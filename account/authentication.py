from django.contrib.auth import authenticate
from django.contrib.auth.backends import BaseBackend

from account.models import User


class CustomAuthenticationUser(BaseBackend):

    def authenticate(self, request, phone=None, password=None):
        try:
            user = User.objects.get(phone=phone)
            if user.chack_password(password):
                return user
            else:
                return password
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


