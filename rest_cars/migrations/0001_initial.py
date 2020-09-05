# Generated by Django 3.1.1 on 2020-09-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(max_length=30)),
                ('model_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_rates', to='rest_cars.car')),
            ],
        ),
    ]
