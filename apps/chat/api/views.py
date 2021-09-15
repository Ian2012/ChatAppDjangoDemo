from rest_framework.generics import DestroyAPIView

from apps.chat.api.serializers import MessageSerializer
from apps.chat.models import Message


class DeleteMessageAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
