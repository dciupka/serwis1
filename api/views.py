from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Geoinfo
from .serializers import GeoinfoSerializer

@api_view(['GET'])
def getData(request,size):
    items = Geoinfo.objects.filter(list_size=size)
    serializer = GeoinfoSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer= GeoinfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)