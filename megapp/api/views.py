from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import Foodhub
from .serializers import FoothubSerializers
from rest_framework import status
# Create your views here.


class FoothubApiView(APIView):
    def get(self, request):
        foodhub = Foodhub.objects.all()
        serializer = FoothubSerializers(instance=foodhub, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

