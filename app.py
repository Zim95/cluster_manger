# third-party
from flask import Flask
from flask_restful import Api

# module
from config import app_settings
from apis import Cluster, Machine, Ping

flask_app = Flask(__name__)
api = Api(flask_app)

# add resources : api.add_resource(<Route-Handler>, '<Route>')
api.add_resource(Ping, '/ping')
api.add_resource(Cluster, '/cluster')
api.add_resource(Machine, '/machine')


if __name__ == "__main__":

    flask_app.run(
        host=app_settings.APP_HOST,
        port=app_settings.APP_PORT,
        debug=True,
        use_reloader=True
    )