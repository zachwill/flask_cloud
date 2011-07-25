#!/usr/bin/env python

"""
In a DotCloud production environment, this script will return a callable
`application` variable that will be run with the uWSGI server.
"""

from app import create_app
application = create_app()
