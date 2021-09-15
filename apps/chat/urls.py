from django.urls import path

from .views import Chat, Login, Signup, Logout

app_name = 'chat'
urlpatterns = [
    path('', Chat.as_view(), name='chat'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
]
