import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        pk = text_data_json['id']
        user = text_data_json['user']
        username = text_data_json['username']
        image = text_data_json['image']
        timestamp = text_data_json['timestamp']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'id': pk,
                'user': user,
                'username': username,
                'image': image,
                'timestamp': timestamp
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        pk = event['id']
        user = event['user']
        username = event['username']
        image = event['image']
        timestamp = event['timestamp']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'id': pk,
            'user': user,
            'username': username,
            'image': image,
            'timestamp': timestamp
        }))
