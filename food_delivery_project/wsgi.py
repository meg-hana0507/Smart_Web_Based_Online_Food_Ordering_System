import os
import sys

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_project.settings')

application = get_wsgi_application()

try:
    call_command('migrate', interactive=False)
    from mainapp.models import User
    if not User.objects.filter(email='admin@gmail.com').exists():
        User.objects.create(
            name='Admin',
            email='admin@gmail.com',
            password='admin',
            role='admin'
        )
except Exception as e:
    print(f"WSGI auto-migration error: {e}")

app = application
