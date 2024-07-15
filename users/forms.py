from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    """Класс формы для регистрации"""
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


