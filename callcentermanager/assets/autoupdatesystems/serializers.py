from rest_framework import serializers  # import de serializers
from assets.models import *

class GetAutoupdatesystemsNameSerializer(serializers.ModelSerializer):
    model = Autoupdatesystems
    fields = ('id', 'name')