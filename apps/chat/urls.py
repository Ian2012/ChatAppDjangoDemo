from django.urls import path

from .views import Chat, Login, Signup

app_name = 'chat'
urlpatterns = [
    path('', Chat.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view()),
]
