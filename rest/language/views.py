from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *

class LanguageView(viewsets.ModelViewSet):
	queryset=Languages.objects.all()
	serializer_class=LanguageSerializer

class paradigmView(viewsets.ModelViewSet):
	queryset=paradigm.objects.all()
	serializer_class=paradigmSerializer

class programmerView(viewsets.ModelViewSet):
	queryset=programmer.objects.all()
	serializer_class=programmerSerializer