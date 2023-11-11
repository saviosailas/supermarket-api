from flask import Flask, request, abort
from flask_restx import Api, Resource

app = Flask(__name__)

app.config['ERROR_404_HELP'] = 0

api = Api(app)

@api.route("/login/")
class Login(Resource):
	"""Return html webpage for login"""
	def get(self):
		return {"message": "GET Request is not allowded"}, 400
		
	def post(self):
		username = request.form.get("username")
		if username is None:
			username = "user"
		return {"message": "login failed for {username}".format(username=username)}, 403

class Django(Resource):
	def get(self, id):
		abort(404, "This is flask framework!")
		
api.add_resource(Django, "/django/<string:id>")
		
if __name__ == "__main__":
	from socket import gethostname
	if "liveconsole" not in gethostname():
		app.run(DEBUG=True)

    
    
