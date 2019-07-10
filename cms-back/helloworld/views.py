# pages/views.py
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Coordinator, IntakeSource, Cat, FosterHome
from .serializers import CoordinatorSerializer, IntakeSourceSerializer, CatSerializer, FosterHomeSerializer


def homePageView(request):
    return HttpResponse('Hello, World!')

class ViewTemplate(APIView):
	def __init__(self, model, serializer):
	       self.model = model
	       self.serializer = serializer
	def get(self, request):
	       model = self.model.objects.all()
	       serializer = self.serializer(model, many=True)
	       return Response(serializer.data)
	def post(self, request):
	       serializer = self.serializer(data=request.DATA)
	       if serializer.is_valid():
	           serializer.save()
	           return Response(serializer.data, status=status.HTTP_201_CREATED)
	       else:
	           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

CatView = ViewTemplate(Cat, CatSerializer)
IntakeSourceView = ViewTemplate(IntakeSource, IntakeSourceSerializer)
CoordinatorView = ViewTemplate(Coordinator, CoordinatorSerializer)
FosterHomeView = ViewTemplate(FosterHome, FosterHomeSerializer)
 
