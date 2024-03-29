
from rest_framework import serializers  # import de serializers
from assets.models import Autoupdatesystems

class GetAutoupdatesystemsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoupdatesystems
        fields = ['id', 'name']

class AutoupdatesystemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autoupdatesystems
        fields = '__all__'