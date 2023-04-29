from rest_framework import serializers  # import de serializers
from assets.models import States

class GetStatesNameSerializer(serializers.ModelSerializer):
    model = States
    fields = ('id', 'name')