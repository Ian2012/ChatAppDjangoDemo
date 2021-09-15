from rest_framework import serializers

from apps.chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'user', 'image', 'timestamp', 'username')
