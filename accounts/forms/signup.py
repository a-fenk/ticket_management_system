from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    pass

    class Meta:
        model = User
        fields = ('username', 'groups', 'password1', 'password2')
