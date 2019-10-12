from rest_framework import serializers
from .models import *

class ListsSerializer(serializers.Serializer):
	id=serializers.IntegerField(read_only=True)
	title=serializers.CharField(required=True, allow_blank=False, max_length=100)
	desc=serializers.CharField(style={'base_template': 'textarea.html'})
	status=serializers.CharField(required=True)
	#created_time=serializers.DateTimeField(auto_now_add=True)
	
	def create(self, validated_data): #validated_data is key value pair
		return Todo.objects.create(**validated_data)
	
	def update(self,instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.sesc=validated_data.get('Desc',instance.desc)
		instance.status=validated_data.get('status',instance.status)
		instance.created_time=validated_data.get('created_time',instance.created_time)
		instance.save()
		return instance