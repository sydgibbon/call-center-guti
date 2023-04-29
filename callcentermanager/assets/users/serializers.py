from rest_framework import serializers  # import de serializers
from assets.models import Users

class GetUsersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name']