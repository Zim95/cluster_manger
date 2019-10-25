from flask_restful import Resource


class Ping(Resource):

    def get(self):
        return 'PONG'


class Cluster(Resource):

    def get(self):
        # Retrieve Cluster
        pass

    def post(self):
        # Create cluster
        pass

    def put(self):
        # Update cluster
        pass

    def delete(self):
        # Delete Cluster
        pass


class Machine(Resource):

    def get(self):
        # Retrieve Machine Details
        pass

    def post(self):
        # Create Machine
        pass

    def put(self):
        # Update Machine Details
        pass

    def delete(self):
        # Delete Machine
        pass
