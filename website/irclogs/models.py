from django.db import models

class IRCLog(models.Model):
    nick = models.CharField(max_length=100)
    channel = models.CharField(max_length=200)    
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} <{}>: {}".format(self.created_at, self.nick, self.message)
