# pages/views.py
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Coordinator, IntakeSource
from .serializers import CoordinatorSerializer, IntakeSourceSerializer


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

@api_view(['GET', 'POST'])
def IntakeSourceView(request):
   if request.method == 'GET':
       coordinator = IntakeSource.objects.all()
       serializer = IntakeSourceSerializer(coordinator, many=True)
       return Response(serializer.data)
   elif request.method == 'POST':
       serializer = IntakeSourceSerializer(data=request.DATA)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

