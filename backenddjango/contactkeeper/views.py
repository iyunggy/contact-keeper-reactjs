from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

class ContactViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ContactSerializers
    queryset = models.Contact.objects.all()