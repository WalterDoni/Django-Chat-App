from datetime import date
from django.conf import settings
from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=500)
    #chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    created_at = models.DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
#chat = Chat Klasse verknüpfen
#Direkt auswählen aus den registrieten User im Admin Infterface
#on_delete -> Sollte ein User gelöscht werden, so werden alle Nachrichten entfernt
#related_name -> Information für die Datenbank, damit diese weiß worum es geht.
