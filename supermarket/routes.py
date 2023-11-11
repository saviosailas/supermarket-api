# Resouces for REST API

from flask import request
from flask_restx import Resource

class Login(Resource):
	"""Return html webpage for login"""
	def get(self):
		return {"message": "GET Request is not allowded"}, 400
		
	def post(self):
		username = request.form.get("username")
		if username is None:
			username = "user"
		return {"message": "login failed for {username}".format(username=username)}, 403
