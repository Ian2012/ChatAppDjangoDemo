from django.urls import path

from .views import DeleteMessageAPIView

app_name = 'chat_api'
urlpatterns = [
    path('delete/<int:pk>', DeleteMessageAPIView.as_view(), name='delete-message'),
]
