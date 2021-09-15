from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic


class Chat(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/chat.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'


class Login(LoginView):
    template_name = 'chat/login.html'


class Logout(LogoutView):
    pass


class Signup(generic.TemplateView):
    template_name = 'chat/signup.html'
