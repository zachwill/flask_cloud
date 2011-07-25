#!/usr/bin/env python

"""
In DotCloud's production environment, this script will be run to
serve your Flask application with uWSGI.
"""

from app import create_app
application = create_app()
