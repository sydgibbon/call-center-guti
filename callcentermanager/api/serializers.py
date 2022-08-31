from dataclasses import field
from rest_framework import serializers
from callcenterdata.models import Computers

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = '__all__'