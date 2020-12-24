from PIL import Image

from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras import backend as K

import numpy as np
import glob
import os

class Predictor:
        def __init__(self, path: str) -> None:
                K.clear_session()
                self.model_path = os.path.join(os.getcwd(), "homestorage", "ml_model", "models", "model.h5")
                self.model_weights_path = os.path.join(os.getcwd(), "homestorage", "ml_model", "models", "weights.h5")
                self.working_dir = os.path.join(os.getcwd(), "homestorage", "ml_model", "data", "alien_test")
                self.image_path = path
                self.model = load_model(self.model_path)
                self.model.load_weights(self.model_weights_path)
                self.model._make_predict_function()

        def resize_and_rotate_images(self) -> None:
                img = Image.open(self.image_path)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img.save(os.path.join(self.working_dir, "1.jpg"))

                for i in range(2, 5):
                        img = img.rotate(90)
                        img.save(os.path.join(self.working_dir, f"{i}.jpg"))

        def remove_images(self) -> None:
                images = glob.glob(os.path.join(self.working_dir, "*.jpg"))

                for image in images:
                        os.remove(image)

        def predict(self) -> int:
                self.resize_and_rotate_images()

                images = glob.glob(os.path.join(self.working_dir, "*.jpg"))
                results = []

                for image_path in images:
                        x = load_img(image_path, target_size=(150, 150))
                        x = img_to_array(x)
                        x = np.expand_dims(x, axis=0)
                        
                        prediction = self.model.predict(x)

                        result = prediction.argmax()
                        results.append(result)

                
                self.remove_images()

                return round(sum(results) / 4)
