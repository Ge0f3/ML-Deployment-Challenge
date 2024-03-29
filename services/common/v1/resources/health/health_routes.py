import logging
import datetime
import time

from flask import request, abort, jsonify
from flask_restplus import Resource, Namespace

log = logging.getLogger(__name__)

ns = Namespace('health', description='Check health of the service')

@ns.route('')
class HealthCheck(Resource):
    def get(self): 
        return jsonify({
            "statusCode": 200, "message": "Everything looks fine", "error": None
        })