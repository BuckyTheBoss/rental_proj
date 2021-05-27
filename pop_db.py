import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rental_proj.settings')
django.setup()

from rent.models import *

fake = Faker()

def pop_customers(number):
    for _ in range(number):
        print(f'creating customer object {_+1}/{number}')
        fname = fake.first_name()
        lname = fake.last_name()
        Customer.objects.create(
            first_name=fname,
            last_name= lname,
            email=f'{fname}.{lname}@example.com',
            phone_number=fake.phone_number(),
            address= fake.street_address(),
            city= fake.city(),
            country= fake.country(),
        )


def pop_vehicle_size():
    labels = ['small', 'medium', 'large', 'double']
    for label in labels:
        obj, created = VehicleSize.objects.get_or_create(name=label)
        if created:
            print('new object create')
        else:
            print('object retrieved')


def pop_vehicle_type():
    labels = ['bike', 'electric bike', 'scooter', 'jetpack']
    for label in labels:
        obj, created = VehicleType.objects.get_or_create(name=label)
        if created:
            print('new object create')
        else:
            print('object retrieved')



def pop_vehicles(number):
    if Vehicle.objects.all().count() < 20:
        for _ in range(number):
            random_type = random.choice(VehicleType.objects.all())
            random_size = random.choice(VehicleSize.objects.all())
            Vehicle.objects.create(
                vehicle_type=random_type,
                real_cost=random.randint(23,100),
                vehicle_size=random_size
            )



if Customer.objects.count() < 40:
    pop_customers(20)
pop_vehicle_size()
pop_vehicle_type()
pop_vehicles(40)