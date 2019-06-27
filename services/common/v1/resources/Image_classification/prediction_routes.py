import logging
from flask import request,jsonify
import json 
from flask_restplus import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage
from services.common.v1.resources.Image_classification.ServiceLayer import ServiceLayer
from services.common.v1.schemas.image_classification_schemas import image_classification_schema


log = logging.getLogger(__name__)

ns = Namespace('per', description='Image Prediction Route')


parser = reqparse.RequestParser()
parser.add_argument('file', location='files', type=FileStorage)
parser.add_argument('path')


@ns.route('/getstatus')
class GetStatus(Resource):
    def get(self):
        try:
            return jsonify({
                'model version ':'1.0'
            }) 
        except Exception as E:
            return jsonify({
                "Error":E
            })

@ns.route('/predict')
class Upload(Resource):
    def post(self):
        '''upload image to get prediction about the image'''
        try:
            return jsonify({
                'prediction':'prediction'
            })

        except Exception as E:
            print(E)
            return jsonify({'Error':"The error is {}".format(E)})
        

       
