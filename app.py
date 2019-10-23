from flask import Flask
from flask_restful import Api

from apis import Cluster, Machine

flask_app = Flask(__name__)
api = Api(flask_app)

# add resources : api.add_resource(<Route-Handler>, '<Route>')
api.add_resource(Cluster, '/cluster')
api.add_resource(Machine, '/machine')


if __name__ == "__main__":

    flask_app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )