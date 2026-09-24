import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_project.settings')

import django
django.setup()

from django.core.management import call_command
from mainapp.models import User

# Automatically run migrations on Vercel container start
try:
    call_command('migrate', interactive=False)
    # Automatically seed default admin if not existing
    if not User.objects.filter(email='admin@gmail.com').exists():
        User.objects.create(
            name='Admin',
            email='admin@gmail.com',
            password='admin',
            role='admin'
        )
except Exception as e:
    print(f"Migration / Auto-seed error: {e}")

from food_delivery_project.wsgi import application

app = application
