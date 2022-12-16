from rest_framework import serializers

from .models import UsersBot

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersBot
        fields = "__all__"