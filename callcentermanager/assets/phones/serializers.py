
from rest_framework import serializers  # import de serializers
from assets.models import Phones, Phonetypes, Phonemodels, Phonepowersupplies

class GetPhonesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['id', 'name']

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