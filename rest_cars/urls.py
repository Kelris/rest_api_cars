from django.urls import path
from .view_external_api import CarsView
from .views import VoteView, PopularView, CarDetailUpdateDelete


urlpatterns = [
    path('cars', CarsView.as_view(), name='cars'),
    path('rate', VoteView.as_view(), name='rate'),
    path('popular', PopularView.as_view(), name='popular'),

    path('car-update/<id>', CarDetailUpdateDelete.as_view(), name='car_update'),
]
