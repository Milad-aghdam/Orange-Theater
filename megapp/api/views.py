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
# Create your views here.


class FoothubApiView(APIView):
    def get(self, request):
        foodhub = Foodhub.objects.all()
        serializer = FoothubSerializers(instance=foodhub, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class JusteatApiView(APIView):
    def get(self, request):
        justeat = Justeat.objects.all()
        serializer = JusteatSerializers(instance=justeat, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class WTFapiView(APIView):
    def get(self, request):
        wtf = WTF.objects.all()
        serializer = WtfSerializers(instance=wtf, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UberEatsApiView(APIView):
    def get(self, request):
        uberEats = UberEats.objects.all()
        serializer = UberEatsSerializers(instance=uberEats, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
