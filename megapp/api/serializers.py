from rest_framework import serializers
from company.models import (
    Foodhub,
    Justeat,
    WTF,
    UberEats,
)

# api serializer foothub


class FoothubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foodhub
        fields = '__all__'


class JusteatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Justeat
        fields = '__all__'


class WtfSerializers(serializers.ModelSerializer):
    class Meta:
        model = WTF
        fields = '__all__'


class UberEatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UberEats
        fields = '__all__'


