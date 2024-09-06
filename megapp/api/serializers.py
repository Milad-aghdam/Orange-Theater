from rest_framework import serializers
from company.models import (
    Foodhub,
    Justeat,
    WTF,
    UberEats,
)

# api serializer foothub


class FoothubSerializers(serializers.ModelSerializer):
        def __init__(self, *args, **kwargs):
            fields = kwargs.pop('fields', None)
            super().__init__(*args, **kwargs)
            
            if fields is not None:
                allowed = set(fields)
                existing = set(self.fields)
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
        class Meta:
            model = Foodhub
            fields = '__all__'


class JusteatSerializers(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:

            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Justeat
        fields = '__all__'


class WtfSerializers(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)  # دریافت فیلدها از kwargs
        super().__init__(*args, **kwargs)

        if fields is not None:
            # حذف فیلدهایی که در `fields` نیستند
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = WTF
        fields = '__all__'


class UberEatsSerializers(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)  # دریافت فیلدها از kwargs
        super().__init__(*args, **kwargs)

        if fields is not None:
            # حذف فیلدهایی که در `fields` نیستند
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = UberEats
        fields = '__all__'

