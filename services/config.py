import os
import json

class RequiredConstants(object):
    # Disable extra message
    ERROR_404_HELP = False

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    # DynamoDB settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'AKIA456TKV7QCV6GY4FJ')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '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')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-2')

    BUCKET_NAME = os.getenv('BUCKET_NAME', '5411model')
    
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
    MONGODB_DB = os.getenv('MONGODB_DB', 'vector')
    USAGE_SERVICE = os.getenv('USAGE_SERVICE', 'http://localhost:4110')
    QUEUE_SERVICE = os.getenv('QUEUE_SERVICE', 'http://localhost:5095')