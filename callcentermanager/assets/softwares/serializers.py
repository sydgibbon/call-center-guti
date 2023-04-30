
from rest_framework import serializers  # import de serializers
from assets.models import Softwarecategories
class GetSoftwarecategoriesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwarecategories
        fields = ['id', 'name']