from os import stat
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country  = models.CharField(max_length=200)
    created_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='customers/', null=True)

    def image(self):
        if self.pic:
            return self.pic.url
        else:
            return static('img/user_default_pic.jpg')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE )
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    vehicle_size = models.ForeignKey('rent.VehicleSize', on_delete=models.CASCADE)
    created_by = models.ForeignKey('accounts.Profile',on_delete=models.PROTECT)
    image_link = models.URLField(null=True)

    def __str__(self):
        return f'Vehicle {self.id} cost: {self.real_cost}'

    def image(self):
        if self.image_link:
            return self.image_link
        else:
            return static('img/default_car.webp')


class VehicleType(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='vehicle_types/', default='vehicle_types/default.jpg')

    def __str__(self):
        return self.name




class VehicleSize(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Rental(models.Model):

    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RentalRate(models.Model):

    daily_rate = models.FloatField()
    vehicle_type =  models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)




       

