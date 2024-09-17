from rest_framework.generics import ListAPIView
from company.models import (
    Foodhub,
    Justeat,
    WhatTheFork,
    UberEats,
    Foodhouse,
    Mealzo,
)
from googlebusiness.models import Account, BusinessInformation
from .serializers import (
    FoothubSerializers,
    JusteatSerializers,
    WsSerializers,
    UberEatsSerializers,
    FoodhouseSerializers,
    MealzoSerializers,
    AccountGoogleSerializers,
    BusinessInformationSerializers
)
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle , AnonRateThrottle
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response





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


class MealzoApiView(ListAPIView):
    queryset = Mealzo.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ['name']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # permission_classes = [IsAuthenticated]

    # pagination_class = PageNumberPagination
    serializer_class = MealzoSerializers

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)


class AccountGoogleApiView(ListAPIView):
    queryset = Account.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    # search_fields = ['name', 'description']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = AccountGoogleSerializers

    # permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)



class BusinessInformationApiView(ListAPIView):
    queryset = BusinessInformation.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    # search_fields = ['name', 'description']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # pagination_class = PageNumberPagination
    serializer_class = BusinessInformationSerializers

    # permission_classes = [IsAuthenticated]
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     count = queryset.count()
    #     return Response({
    #         'count': count,
    #         'results': serializer.data
    #     })

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)