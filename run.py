
#!/usr/bin/env python
import os
import sys
import webbrowser
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supermarketten.settings")
#these pertain to your application
import supermarketten.wsgi
import supermarketten.urls
import supermarketten.settings
import supermarketten.models
import supermarketten.views

import django.contrib.auth
import django.contrib.contenttypes
import django.contrib.sessions
import django.contrib.sites
import django.contrib.admin

import django.db.models.sql.compiler
from django.contrib.auth.backends import *
from django.conf.urls.defaults import *
#these are django imports
import django.template.loaders.filesystem
import django.template.loaders.app_directories
import django.middleware.common
import django.contrib.sessions.middleware
import django.contrib.auth.middleware
import django.middleware.doc
import django.contrib.messages
import django.contrib.staticfiles
import django.contrib.messages.middleware
import django.contrib.sessions.backends.db
#import django.contrib.messages.storage.user_messages
import django.contrib.messages.storage.fallback
import django.db.backends.sqlite3.base
import django.db.backends.sqlite3.introspection
import django.db.backends.sqlite3.creation
import django.db.backends.sqlite3.client
import django.contrib.auth.context_processors
from django.core.context_processors import *
import django.contrib.messages.context_processors
import django.contrib.auth.models
import django.contrib.contenttypes.models
import django.contrib.sessions.models
import django.contrib.sites.models
import django.contrib.messages.models
import django.contrib.staticfiles.models
import django.contrib.admin.models
import django.template.defaulttags
import django.template.defaultfilters
import django.template.loader_tags
#dont need to import these pkgs
#need to know how to exclude them
import email.mime.audio
import email.mime.base
import email.mime.image
import email.mime.message
import email.mime.multipart
import email.mime.nonmultipart
import email.mime.text
import email.charset
import email.encoders
import email.errors
import email.feedparser
import email.generator
import email.header
import email.iterators
import email.message
import email.parser
import email.utils
import email.base64mime
import email.quoprimime
import django.core.cache.backends.locmem
import django.templatetags.i18n
import django.templatetags.future
import django.views.i18n
import django.core.context_processors
import django.template.defaulttags
import django.template.defaultfilters
import django.template.loader_tags
from django.conf.urls.defaults import *
import django.contrib.admin.views.main
import django.core.context_processors
import django.contrib.auth.views
import django.contrib.auth.backends
import django.views.static
import django.contrib.admin.templatetags.log
import django.contrib.admin.templatetags.adminmedia
import django.conf.urls.shortcut
import django.views.defaults
from django.core.handlers.wsgi import WSGIHandler
from django.core.servers.basehttp import AdminMediaHandler
from django.conf import settings
from django.utils import translation
import django.contrib.staticfiles.urls

if __name__ == "__main__":
    if len(sys.argv)==1:
        sys.argv.append("runserver")
        sys.argv.append("0.0.0.0:8000")
    else:
        webbrowser.open_new_tab('http://127.0.0.1:8000')
    print sys.argv
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
