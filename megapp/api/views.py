from rest_framework.generics import ListAPIView
from company.models import (
    Foodhub,
    Justeat,
    WTF,
    UberEats,
    Foodhouse,
)
from .serializers import (
    FoothubSerializers,
    JusteatSerializers,
    WtfSerializers,
    UberEatsSerializers,
    FoodhouseSerializers,
)
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets



# Create your views here.


class FoothubApiView(ListAPIView):
    queryset = Foodhub.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name', 'description']
    # pagination_class = PageNumberPagination
    serializer_class = FoothubSerializers
    
    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)
    
    


class JusteatApiView(ListAPIView):
    queryset = Justeat.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name']
    # pagination_class = PageNumberPagination
    serializer_class = JusteatSerializers

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)



class FoodhouseApiView(ListAPIView):
    queryset = Foodhouse.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name']
    # pagination_class = PageNumberPagination
    serializer_class = FoodhouseSerializers

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)


class WTFapiView(ListAPIView):
    wtf = WTF.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    # pagination_class = PageNumberPagination
    serializer_class = WtfSerializers

class UberEatsApiView(ListAPIView):
    queryset = UberEats.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    # pagination_class = PageNumberPagination
    serializer_class = UberEatsSerializers

