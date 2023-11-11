from flask import Flask, request
from flask_restx import Api, Resource, abort
from .urls import public_ns

app = Flask(__name__)

app.config['ERROR_404_HELP'] = 0

api = Api(app)



api.add_namespace(public_ns)
		
@api.route("/django/<string:id>", strict_slashes=0)
class Django(Resource):
	def get(self, id):
		abort(404, "This is flask framework!")
		
		
if __name__ == "__main__":
	from socket import gethostname
	if "liveconsole" not in gethostname():
		app.run(DEBUG=True)

    
    
