from rest_framework.generics import ListAPIView
from company.models import (
    Foodhub,
    Justeat,
    WhatTheFork,
    UberEats,
    Foodhouse,
)
from .serializers import (
    FoothubSerializers,
    JusteatSerializers,
    WsSerializers,
    UberEatsSerializers,
    FoodhouseSerializers,
)
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle , AnonRateThrottle
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS





# Create your views here.


class FoothubApiView(ListAPIView):
    queryset = Foodhub.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name', 'description']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = FoothubSerializers
    # permission_classes = [IsAuthenticated]
    
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
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = JusteatSerializers
    # permission_classes = [IsAuthenticated]


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
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = FoodhouseSerializers
    # permission_classes = [IsAuthenticated]


    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)


class UberEatsApiView(ListAPIView):
    queryset = UberEats.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = UberEatsSerializers
    # permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)


class WsApiView(ListAPIView):
    queryset = WhatTheFork.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # permission_classes = [IsAuthenticated]


    # pagination_class = PageNumberPagination
    serializer_class = WsSerializers

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)

