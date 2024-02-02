from datetime import date
from django.conf import settings
from django.db import models

class Chat(models.Model):
    created_at = models.DateField(default=date.today)

class Message(models.Model):
    text = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    created_at = models.DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
#chat = blank=Null der Standartwert ist nichts, blank=True es darf nichts hineingegeben werden, null=True Datenbank akzeptiert auf nichts
#Wird benötigt falls im Laufe das Model erweitert wird und ältere Nachrichten ohne dem chat keinen Fehler aufweisen.
#author -> Direkt auswählen aus den registrieten User im Admin Infterface
#on_delete -> Sollte ein User gelöscht werden, so werden alle Nachrichten entfernt
#related_name -> Information für die Datenbank, damit diese weiß worum es geht.
