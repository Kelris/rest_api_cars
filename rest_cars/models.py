from django.db import models
from django.db.models import Avg


class Car(models.Model):
    make_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)

    def __str__(self):
        return self.make_name.lower() + " " + self.model_name.lower()

    def get_average_rate(self):
        average_rate = self.car_rates.all().aggregate((Avg('rate')))['rate__avg']
        return average_rate


class Vote(models.Model):
    car = models.ForeignKey(Car, related_name='car_rates', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return str(self.car) + " : " + str(self.rate)
