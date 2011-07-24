#!/usr/bin/env python

"""
Bootstrap and run your application.

If you're in a development environment, envoke the script with:
    $ python bootstrap.py --dev

In a production environment, the `gevent` library will be used to serve up the
application. In that case, envoke the script without the `--dev` argument:
    $ python bootstap.py

"""

import argparse

from app import create_app
from gevent.wsgi import WSGIServer


def parse_arguments():
    """Parse any additional arguments that may be passed to `bootstrap.py`."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', action='store_true',
                        help="Turn Flask's development server on.")
    args = parser.parse_args()
    return args.dev


def serve_app(dev_environment):
    """
    Serve your application. If `dev_environment` is true, then the
    application will be served using Flask's development server.
    """
    app = create_app()
    if dev_environment:
        app.run(debug=True)
    else:
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()


def main():
    dev_environment = parse_arguments()
    serve_app(dev_environment)

if __name__ == '__main__':
    main()
