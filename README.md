## rest_api_cars
Live Version: [https://rest-api-cars.herokuapp.com/](https://rest-api-cars.herokuapp.com/ "Heroku (live version)")

This is cars makes and models database using Django Rest Framework. It interacts with external API (https://vpic.nhtsa.dot.gov/api/).

1. Clone this repository:

```git clone https://github.com/Kelris/rest_api_cars.git```

2. Create virtual environment: 

```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

3. Install requirements:
 
```pip install -r requirements.txt```

4. Connect to your database and run following commands:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  
```
