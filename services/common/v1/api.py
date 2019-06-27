import logging

from flask_restplus import Api

from services.blueprints import common_blueprint_v1

from services.common.v1.resources.Image_classification.prediction_routes import ns as prediction_routes
from services.common.v1.resources.health.health_routes import ns as health_routes

log = logging.getLogger(__name__)

api = Api(common_blueprint_v1,
          version='1.0',
          title='ML Deployment Challenge',
          description='description for api')

# prefixes
image_classifier = '/image_classification'
health = '/health'

api.add_namespace(prediction_routes,path=image_classifier)
api.add_namespace(health_routes, path=health)

