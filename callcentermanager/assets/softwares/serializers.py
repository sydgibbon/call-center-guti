
from rest_framework import serializers  # import de serializers
from assets.models import Softwarecategories, Softwares, Softwarelicenses
class GetSoftwarecategoriesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = ['id', 'name']

class GetSoftwaresCountSerializer(serializers.ModelSerializer):
    softwaresCount = serializers.SerializerMethodField()
    
    def get_softwaresCount(self,obj):
        return Softwares.objects.count()
    
    class Meta:
        model = Softwares
        fields = ['softwaresCount']

class GetSoftwarelicensesCountSerializer(serializers.ModelSerializer):
    softwarelicensesCount = serializers.SerializerMethodField()
    
    def get_softwarelicensesCount(self,obj):
        return Softwarelicenses.objects.count()
    
    class Meta:
        model = Softwarelicenses
        fields = ['softwarelicensesCount']