from django.urls import path

from .views import DeleteMessageAPIView, ListCreateMessageAPIView

app_name = 'chat_api'
urlpatterns = [
    path('delete/', DeleteMessageAPIView.as_view(), name='delete-message'),
    path('messages/', ListCreateMessageAPIView.as_view(), name='list-create-message'),
]
