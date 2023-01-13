from django.shortcuts import render
# import viewsets
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
