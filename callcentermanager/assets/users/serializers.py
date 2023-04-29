from rest_framework import serializers  # import de serializers
from assets.models import Users

class GetUsersNameSerializer(serializers.ModelSerializer):
    model = Users
    fields = ('id', 'name')