from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import (
    Foodhub,
    Justeat,
    WTF,
    UberEats
)
from .serializers import (
    FoothubSerializers,
    JusteatSerializers,
    WtfSerializers, UberEatsSerializers,
)
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


# Create your views here.


class FoothubApiView(ListAPIView):
    queryset = Foodhub.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    pagination_class = PageNumberPagination
    serializer_class = FoothubSerializers


class JusteatApiView(ListAPIView):
    queryset = Justeat.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    pagination_class = PageNumberPagination
    serializer_class = JusteatSerializers


class WTFapiView(ListAPIView):
    wtf = WTF.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    pagination_class = PageNumberPagination
    serializer_class = WtfSerializers

class UberEatsApiView(ListAPIView):
    queryset = UberEats.objects.all()
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
    pagination_class = PageNumberPagination
    serializer_class = UberEatsSerializers
