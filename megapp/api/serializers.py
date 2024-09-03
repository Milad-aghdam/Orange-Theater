from rest_framework import serializers
from company.models import Foodhub

# api serializer foothub


class FoothubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foodhub
        fields = '__all__'

