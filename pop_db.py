import os
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rental_proj.settings')
django.setup()

from rent.models import *

fake = Faker()



