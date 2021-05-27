from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country  = models.CharField(max_length=200)


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE )
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    vehicle_size = models.ForeignKey('rent.VehicleSize', on_delete=models.CASCADE)


class VehicleType(models.Model):
    name = models.CharField(max_length=200)


class VehicleSize(models.Model):
    name = models.CharField(max_length=200)


class Rental(models.Model):

    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RentalRate(models.Model):

    daily_rate = models.FloatField()
    vehicle_type =  models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)