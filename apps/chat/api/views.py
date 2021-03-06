from rest_framework import pagination
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, get_object_or_404

from apps.chat.api.serializers import MessageSerializer
from apps.chat.models import Message


class DeleteMessageAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_object(self):
        return get_object_or_404(Message, id=self.request.query_params.get('detalle'))


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class ListCreateMessageAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
