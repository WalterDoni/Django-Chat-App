from django.contrib import admin
from .models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text', 'created_at', 'author', 'receiver')
    list_display = ('created_at', 'author', 'text', 'receiver')
    search_fields = ('author',)


admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)