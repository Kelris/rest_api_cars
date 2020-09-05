import requests
from rest_framework import generics
from rest_framework.exceptions import APIException, NotFound
from rest_framework.response import Response
from rest_cars.models import Car
from rest_cars.serializers import CarSerializer


class CarsView(generics.ListCreateAPIView):
    queryset = Car.objects.all().order_by('make_name')
    serializer_class = CarSerializer

    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        make_name = str(request.data['make_name']).upper()
        model_name = str(request.data['model_name']).upper()
        response = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make_name}?format=json')
        if serializer.is_valid():
            if '"' + make_name + '"' in response.text.upper():
                if (('"' + model_name + '"') in response.text.upper()) or (('/' + model_name + '"') in response.text.upper()) or (('"' + model_name + '\\') in response.text.upper()):
                    if model_name.upper() in str(Car.objects.all()).upper():
                        print(model_name.upper())
                        print("This model already exists in your data base.")
                        raise APIException
                    else:
                        serializer.save()
                        print(f"SAVED (make): '{make_name}'" + '\n' + f"SAVED (model): '{model_name}'")
                else:
                    print(f"Model: '{model_name}' does not exist.")
                    raise NotFound
            else:
                print(f"Make: '{make_name}' does not exist.")
                raise NotFound
            return Response(serializer.data)


