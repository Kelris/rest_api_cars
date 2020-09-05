from django.db.models import Count
from rest_framework import generics
from .models import Car, Vote
from .serializers import CarSerializer, VoteSerializer


class VoteView(generics.ListCreateAPIView):
   queryset = Vote.objects.all().order_by('car_id')
   serializer_class = VoteSerializer


class PopularView(generics.ListAPIView):
    queryset = Car.objects.annotate(num_rates=Count('car_rates')).order_by('num_rates').reverse()[:3]
    serializer_class = CarSerializer


class CarDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = "id"
