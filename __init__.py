from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)

@api.route("/login")
class Login(Resource):
	def get(self):
		return {"message": "GET Request is not allowded"}, 400
	def post(self):
		username = request.form.get("username")
		return {"message": "login failed"}, 403


if __name__ == "__main__":
	from socket import gethostname
	if "liveconsole" not in gethostname():
		app.run(DEBUG=True)
