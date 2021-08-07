from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields y exclude son mutuamente excluyentes
        fields = '__all__'

