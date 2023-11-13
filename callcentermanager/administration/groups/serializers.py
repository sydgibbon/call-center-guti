from rest_framework import serializers  # import de serializers
from assets.models import Groups

class GetGroupsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['completename', 'comment']
