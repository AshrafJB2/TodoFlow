from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class PriorityField(serializers.Field):
    """
    Converts string priority to integer and vice versa
    Example:
    - Input: "high" → 3
    - Output: 3 → "high"
    """
    def to_representation(self, value):
        return dict(Todo.PRIORITY_CHOICES).get(value, 'unknown')

    def to_internal_value(self, data):
        reverse_choices = {v.lower(): k for k, v in Todo.PRIORITY_CHOICES}
        try:
            return reverse_choices[data.lower()]
        except KeyError:
            raise serializers.ValidationError(
                f"Invalid priority. Valid choices are: {[choice[1] for choice in Todo.PRIORITY_CHOICES]}"
            )


class TodoSerializer(serializers.ModelSerializer):
    priority = PriorityField()
    
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'priority', 
                 'completed', 'due_date', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
