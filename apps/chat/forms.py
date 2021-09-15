from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from apps.chat.models import Message


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class MessageCreationForm(ModelForm):
    class Meta:
        model = Message
        fields = ('image',)
