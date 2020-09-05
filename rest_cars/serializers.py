from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Car, Vote


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id', 'car', 'rate', ]


class CarSerializer(serializers.ModelSerializer):
    car_rates = StringRelatedField(many=True, read_only=True)
    average_rate = serializers.CharField(source='get_average_rate', read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make_name', 'model_name', 'average_rate', 'car_rates']
