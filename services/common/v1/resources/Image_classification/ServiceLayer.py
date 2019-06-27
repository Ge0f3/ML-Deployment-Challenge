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


log = logging.getLogger(__name__)





class ServiceLayer:

   @staticmethod
   def helloworld():
       return "hellow world"


