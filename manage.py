from services.application import create_app
from services.config import RequiredConstants
from flask_restplus import Resource, Api
from services.common.v1.resources.Image_classification.ServiceLayer import ServiceLayer
import os

app = create_app()
api = Api(app)   
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

@api.route('/')                  
class HelloWorld(Resource):            
    def get(self):                     
        return {'hello': 'world'}

    
if __name__ == "__main__":
    print("<----------loading Keras model and starting Flask server -------->")
    #ServiceLayer.load_model()
    print("Keras model loaded")
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT_PY', '5000')))
