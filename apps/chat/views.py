from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

from apps.chat.forms import UserRegistrationForm


class Chat(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/chat.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'


class Login(LoginView):
    template_name = 'chat/login.html'


class Logout(LogoutView):
    next_page = '/login'


class Signup(generic.CreateView):
    template_name = 'chat/signup.html'
    success_url = '/'
    form_class = UserRegistrationForm
