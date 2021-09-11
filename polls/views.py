from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from .models import Poll
from .serializers import PollSerializer
from datetime import datetime, timedelta

# Create your views here.
class PollList(generics.ListAPIView):
    queryset = Poll.objects.filter()
    serializer_class = PollSerializer


class PollDetails(generics.RetrieveAPIView):
    queryset = Poll.objects.filter()
    serializer_class = PollSerializer
