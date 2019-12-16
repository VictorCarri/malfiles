"""
WSGI config for malayalam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, os.path.abspath("../venv/lib/python3.6/site-packages")) # Add our virtual environment's site-packages to the path so that the WSGI modules will find Django
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))) # Add the project directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) # Add the app directory to Python's path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'malayalam.settings')
application = get_wsgi_application()
