"""app."""


from __future__ import absolute_import, division, print_function

from flask import Flask

from ..base import Base


def create_app(max_ids=None):
    """Create webapp.

    Factory for webapp.

    Returns
    -------
    app : flask.app.Flask
        Flask app object.

    """
    app = Flask(__name__)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.base = Base(max_ids=max_ids)

    return app
