"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# On Vercel the entrypoint is imported as ``src/config/wsgi.py`` with /var/task
# as the working directory, so ``src/`` is not on sys.path and the ``config``
# package can't be found. Add ``src/`` (this file's parent's parent) explicitly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Vercel's Python runtime looks for a module-level ``app`` callable.
app = application
