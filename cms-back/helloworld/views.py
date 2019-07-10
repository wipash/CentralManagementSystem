# pages/views.py
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Coordinator
from .serializers import CoordinatorSerializer


def homePageView(request):
    return HttpResponse('Hello, World!')

@api_view(['GET', 'POST'])
def CoordinatorView(request):
   if request.method == 'GET':
       coordinator = Coordinator.objects.all()
       serializer = CoordinatorSerializer(coordinator, many=True)
       return Response(serializer.data)
   elif request.method == 'POST':
       serializer = CoordinatorSerializer(data=request.DATA)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



