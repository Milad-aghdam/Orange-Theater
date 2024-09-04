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
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# Create your views here.


class FoothubApiView(APIView):
    def get(self, request):
        foodhub = Foodhub.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=foodhub, request=request)
        serializer = FoothubSerializers(instance=result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class JusteatApiView(APIView):
    def get(self, request):
        justeat = Justeat.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=justeat, request=request)
        serializer = JusteatSerializers(instance=result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class WTFapiView(APIView):
    def get(self, request):
        wtf = WTF.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=wtf, request=request)
        serializer = WtfSerializers(instance=result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UberEatsApiView(APIView):
    def get(self, request):
        uberEats = UberEats.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=uberEats, request=request)
        serializer = UberEatsSerializers(instance=result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
