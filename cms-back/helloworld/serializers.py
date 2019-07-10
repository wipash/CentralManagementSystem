from rest_framework import serializers
from .models import Coordinator, IntakeSource

class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ('name', 'type',  'phone_number', 'email')

class IntakeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeSource 
        fields = ('name', 'contact')


'''
class CatClass(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = 
'''
