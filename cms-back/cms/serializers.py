from rest_framework import serializers
from .models import Coordinator, IntakeSource, Cat, FosterHome

#instead of specifying all fields manually, all are exposed

class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = '__all__'

class IntakeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeSource 
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

class FosterHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FosterHome
        fields = '__all__'

