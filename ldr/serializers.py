from rest_framework import serializers
from ldr.models import Message , actions
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Message
        fields = ['id','created','message','actions','read','owner']

class UserSerializer(serializers.ModelSerializer):
    message = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'messages']