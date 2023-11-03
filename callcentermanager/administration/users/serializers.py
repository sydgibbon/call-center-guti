from assets.models import Users
from rest_framework import serializers


class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'phone', 'locations', 'is_active']