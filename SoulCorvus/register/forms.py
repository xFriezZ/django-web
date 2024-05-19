from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer