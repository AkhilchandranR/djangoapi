from rest_framework import serializers
from .models import *

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Languages
		fields=('id','url','name','paradigm')
class paradigmSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=paradigm
		fields=('id','url','name')
class programmerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=programmer
		fields=('id','url','name','language')