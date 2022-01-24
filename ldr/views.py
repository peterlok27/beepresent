from ldr.models import Message 
from ldr.serializers import MessageSerializer
from ldr.permissions import IsOwnerOrReadOnly
from ldr.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions , filters
from django_filters.rest_framework import DjangoFilterBackend



class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all().reverse().order_by('created')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Unread(generics.ListCreateAPIView):
    queryset = Message.objects.filter(read=False).reverse().order_by('created')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]

class SetRead(generics.RetrieveUpdateDestroyAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]