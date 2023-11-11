# URL routes for REST API

from flask_restx import Namespace

from .routes import Login

public_ns = Namespace(name="public", description="List of urls that doesn't require authentication", path="/api/v1")

public_ns.add_resource(Login, "/login", strict_slashes=0)
