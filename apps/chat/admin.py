from django.contrib import admin

# Register your models here.
from apps.chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp']
    list_filter = ['user', 'timestamp']
    search_fields = ['user', 'timestamp']


admin.site.register(Message)
