from services.config import RequiredConstants as RC
import requests
import os
import datetime
import shutil
import PIL.Image as Image
import io
import logging
from flask import request,jsonify
from services.core.Validation import Validation

import numpy as np 
from keras import backend as K  
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
from keras.applications import imagenet_utils
import keras 
from keras.applications import vgg16
import numpy as np 
from PIL import Image
import tensorflow as tf


log = logging.getLogger(__name__)

vgg_model = None


class ServiceLayer:

    
    @classmethod
    def load_model(cls):
        global vgg_model 
        vgg_model= vgg16.VGG16(weights='imagenet')
    
    @staticmethod
    def preprocess_image(image,target):
       #if image mode is not RGB converting it 
       if image.mode != 'RGB':
           image = image.convert('RGB')
       #Resize the input image 
       image = image.resize(target)
       image = img_to_array(image)
    #    image = np.array(image)/255.0
       print("Image shape is {}".format(image.shape))
       image = np.expand_dims(image,axis=0)
       print("The image shape is {}".format(image.shape))
       preprocess_image = imagenet_utils.preprocess_input(image)
       
       #Return the processed image
       return preprocess_image
    
    @classmethod
    def predict_image(cls,processed_image):
       vgg_model = vgg16.VGG16(weights='imagenet')
       graph = tf.get_default_graph()
       with graph.as_default():
           pred = vgg_model.predict(processed_image)


       results = imagenet_utils.decode_predictions(pred)
       
       data = dict()
       data['predictions'] = []
       
       for (imagenet_id,label,prob) in results[0]:
           r = {'label':label,'probability':float(prob)}
           data['predictions'].append(r)

       K.clear_session()

       return data
       
      





