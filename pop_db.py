import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rental_proj.settings')
django.setup()

from rent.models import Vehicle

