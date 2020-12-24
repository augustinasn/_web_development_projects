"""# Test:"""

from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

import numpy as np

import glob
import os

model_path = "./models/model.h5"
model_weights_path = "./models/weights.h5"
test_path = "./data/alien_test"

model = load_model(model_path)
model.load_weights(model_weights_path)

img_width, img_height = 150, 150

def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    result = model.predict(x)

    return result.argmax()

path = os.path.join(os.getcwd(), "data", "alien_test")  
files = glob.glob(path + "/*.jpg")

for file in files:
    prediction = predict(file)
    print(file, "->", prediction)