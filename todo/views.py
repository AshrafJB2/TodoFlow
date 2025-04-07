from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]  # Requires valid token
    
    def get(self, request):
        return Response({"valid": True, "user": request.user.username, 'id': request.user.id})


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class TodoListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'priority']

    def get_queryset(self):
        """Return only the todos belonging to the current user"""
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically set the user to the current user when creating a todo"""
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        """Return only the todos belonging to the current user"""
        return Todo.objects.filter(user=self.request.user)