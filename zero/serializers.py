from rest_framework import serializers #type: ignore
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'name', 'stack']