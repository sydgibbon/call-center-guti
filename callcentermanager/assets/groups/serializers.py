from rest_framework import serializers  # import de serializers
from assets.models import Groups

class GetGroupsNameSerializer(serializers.ModelSerializer):
    model = Groups
    fields = ('id', 'name')