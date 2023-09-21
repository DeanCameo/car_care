import datetime
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    plate_number = models.IntegerField(default=0 ,null=True)
    brand = models.CharField(max_length=15, default='default')
    car_type = models.CharField(max_length=10)
    color = models.CharField(max_length=15, null=True)
    year = models.IntegerField(default=0)
    km = models.IntegerField(default=0)
    test_date = models.DateField(null=True)


class Product(models.Model):
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    product_name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=20)


class Service(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    serv_date = models.DateField(null=True)
    serv_km = models.IntegerField(default=0)
    serv_type = models.CharField(max_length=20)
    serv_price = models.DecimalField(max_digits=10, decimal_places=2)


class Repair(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    repair_date = models.DateField(null=True)
    repaired_parts = models.TextField(default='default')
    breakdown_description = models.TextField(blank=True)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)


class WheelChange(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    tire_date = models.DateField(null=True)
    tire_size = models.CharField(max_length=5)
    tire_km = models.IntegerField(default=0)
    tire_price = models.DecimalField(max_digits=10, decimal_places=2)


class Insurance(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    insurance_start_date = models.DateField(null=True)
    insurance_expiration_date = models.DateField(null=True)
    insurance_company = models.CharField(max_length=100)
    insurance_price = models.DecimalField(max_digits=10, decimal_places=2)


class Fuel(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=20, null=True)
    fuel_amount = models.IntegerField(default=0, null=True)
    station_name = models.CharField(max_length=20, null=True)
    km_per_tank = models.IntegerField(default=0, null=True)
    price_per_gallon = models.IntegerField(default=0, null=True)
    fuel_overall_price = models.IntegerField(default=0, null=True)
    fuel_date = models.DateField(null=True)