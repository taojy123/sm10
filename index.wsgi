"""
import sae
from supermarketten import wsgi

application = sae.create_wsgi_app(wsgi.application)
"""


import sae
import sys,os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'supermarketten.settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())



