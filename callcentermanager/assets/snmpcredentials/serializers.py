from rest_framework import serializers  # import de serializers
from assets.models import Snmpcredentials

class GetSnmpcredentialsSerializer(serializers.ModelSerializer):
    model = Snmpcredentials
    fields = ('id', 'name')