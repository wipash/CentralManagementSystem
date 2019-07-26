# pages/views.py
from django.http import HttpResponse
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Coordinator, IntakeSource, Cat, FosterHome
from .serializers import CoordinatorSerializer, IntakeSourceSerializer, CatSerializer, FosterHomeSerializer


def homePageView(request):  # noqa: N802
    return HttpResponse('Hello, World!')


class CatView(APIView):
    def get(self, request):
        model = Cat.objects.all()
        serializer = CatSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
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
        serializer = IntakeSourceSerializer(data=request.data)
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
        serializer = FosterHomeSerializer(data=request.data)
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
        serializer = CoordinatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatDetailView(APIView):
    def get_object(self, pk):
        try:
            return Cat.objects.get(pk=pk)
        except Cat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = CatSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = CatSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IntakeSourceDetailView(APIView):
    def get_object(self, pk):
        try:
            return IntakeSource.objects.get(pk=pk)
        except IntakeSource.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = IntakeSourceSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = IntakeSourceSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoordinatorDetailView(APIView):
    def get_object(self, pk):
        try:
            return Coordinator.objects.get(pk=pk)
        except Coordinator.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = CoordinatorSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = CoordinatorSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FosterHomeDetailView(APIView):
    def get_object(self, pk):
        try:
            return FosterHome.objects.get(pk=pk)
        except FosterHome.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = FosterHomeSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = FosterHomeSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
