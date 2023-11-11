# supermarket-api
REST API using FlaskRestX framework 
- Swagger UI
- CURD operation
- Authentication
- Role based authentication
- JWT token
 
## Make REST API using flask-restx
1. Create a class that derived from `Resource` class
2. Define the methods for HTTP methods like get, post, pust and delete
3. Using `add_resource()` map the class/resources to urls

```python
from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

class SampleResource(Resource):
  def get(self):
    return {"status": "System operational"}, 200 , {"agent_ip": "192.2.0.13"}
 def post(self):
api.add_resource(SampleResource, "/api/v2/status", "/api/v3/status")

if __name__ == "__main__":
    app.run(DEBUG=True)
```
  
