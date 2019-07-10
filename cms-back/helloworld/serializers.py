from rest_framework import serializers
from .models import Coordinator

class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ('name', 'phone_number')
