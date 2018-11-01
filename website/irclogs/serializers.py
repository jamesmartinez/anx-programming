from rest_framework import serializers
from irclogs.models import IRCLog

class IRCLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRCLog
        fields = ('id', 'nick', 'message', 'created_at')

