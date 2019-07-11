# pages/views.py
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Coordinator, IntakeSource, Cat, FosterHome
from .serializers import CoordinatorSerializer, IntakeSourceSerializer, CatSerializer, FosterHomeSerializer


def homePageView(request):
    return HttpResponse('Hello, World!')


class CatView(APIView):
    def get(self, request):
        model = Cat.objects.all()
        serializer = CatSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IntakeSourceView(APIView):
    def get(self, request):
        model = IntakeSource.objects.all()
        serializer = IntakeSourceSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FosterHomeView(APIView):
    def get(self, request):
        model = FosterHome.objects.all()
        serializer = FosterHomeSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoordinatorView(APIView):
    def get(self, request):
        model = Coordinator.objects.all()
        serializer = CoordinatorSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
