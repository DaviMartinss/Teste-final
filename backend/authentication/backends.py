from django.contrib.auth.backends import ModelBackend
from authentication.models import User

class CPFBackend(ModelBackend):
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        try:
            user = User.objects.get(cpf=cpf)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
