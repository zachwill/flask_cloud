#!/usr/bin/env python

"""
Run your application.

If you're in a development environment, envoke the script with:
    $ python wsgi.py --dev

In a DotCloud production environment, this script will return a callable
`application` variable that will be run with the uWSGI server.
"""

import argparse

from app import create_app


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', action='store_true',
                        help="Turn Flask's development server on.")
    args = parser.parse_args()
    return args.dev


if __name__ == '__main__':
    dev_environment = parse_arguments()
    app = create_app()
    if dev_environment:
        app.run(debug=True)
    else:
        application = app
