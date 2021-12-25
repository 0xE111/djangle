from django.contrib.auth.backends import BaseBackend
from core.models import User


class EmailPasswordBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        if email is None or password is None:
            return

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return

        if user.check_password(password) and user.is_active:
            return user

    def get_user(self, user_id):
        return User.objects.filter(pk=user_id).first()


class EmailAsUsernamePasswordBackend(EmailPasswordBackend):
    """
    This is a hack to allow users login into Django Admin because it uses
    self.user_cache = authenticate(self.request, username=username, password=password)
    """
    def authenticate(self, request, username=None, password=None):
        return super().authenticate(request, email=username, password=password)
