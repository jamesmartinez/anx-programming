from irclogs.models import IRCLog
from irclogs.serializers import IRCLogSerializer
from rest_framework import generics

class IRCLogListCreate(generics.ListCreateAPIView):
    queryset = IRCLog.objects.all()
    serializer_class = IRCLogSerializer
