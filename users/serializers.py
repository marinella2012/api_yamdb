from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        many=False,
        slug_field='username'
    )

    class Meta:
        fields = ('username', 'email', 'role', 'bio', 'first_name', 'last_name')
        model = User
