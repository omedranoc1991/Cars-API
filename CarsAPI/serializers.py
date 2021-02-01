from rest_framework import serializers
from CarsAPI.models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('name', 'brand', 'price')
