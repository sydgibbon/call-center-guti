
from rest_framework import serializers  # import de serializers
from assets.models import Phonetypes, Phonemodels, Phonepowersupplies

class GetPhonetypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetypes
        fields = ['id', 'name']

class GetPhonemodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonemodels
        fields = ['id', 'name']

class GetPhonepowersuppliesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonepowersupplies
        fields = ['id', 'name']