from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'role', 'bio', 'first_name', 'last_name')
        model = User
