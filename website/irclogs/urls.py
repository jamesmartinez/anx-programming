from django.urls import path
from . import views

urlpatterns = [
        path('api/irclogs/', views.IRCLogListCreate.as_view()),
]
