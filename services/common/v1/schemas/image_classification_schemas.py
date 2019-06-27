from flask_restplus import fields, Model


image_classification_schema=Model('Image classification schema',{
    'model_name': fields.String,
})




