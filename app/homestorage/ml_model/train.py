# -*- coding: utf-8 -*-
"""item_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XcewmsWgzZacJ047lcboZW1Tl85F8V46

# Train:
"""

from keras.preprocessing.image import ImageDataGenerator

from keras import optimizers

from keras.models import Sequential

from keras.layers import Dropout, Flatten, Dense, Activation
from keras.layers.convolutional import Convolution2D, MaxPooling2D

train_data_path = 'data/train'
validation_data_path = 'data/test'

# Number of complete passes through the training dataset:
epochs = 20 

# Input shape aka image size:
img_width, img_height = 150, 150 

# Number of samples processed before the model is updated
# (Should be >= 1, but <= size of the dataset.): 
batch_size = 32 

samples_per_epoch = 1000
validation_steps = 300

# The dimensionality of the output space 
# (i.e. the number of output filters in the convolution)
# or in other words -  the number of neurons:
nb_filters1 = 32
nb_filters2 = 64

# kernel_size: An integer specifying the height and width of the 2D convolution window.
# strides: An integer specifying the strides of the convolution along the height and width.
conv1_size = 3
conv2_size = 2

# factors by which to downscale (vertical, horizontal)
# If only one integer is specified, the same window length will be used for both dimensions.
pool_size = 2

# Positive integer, dimensionality of the output space.
# also known as - number of classes being predicted;
classes_num = 2

# Learning rate;
lr = 0.0004

model = Sequential()

# borer_mode is padding (one of "valid" or "same");
# third numeber in shape is the three layers of colors (RGB);
model.add(Convolution2D(nb_filters1, conv1_size, conv1_size, border_mode ="same", input_shape=(img_width, img_height, 3)))

# activation - Rectified Linear Unit, layer:
model.add(Activation("relu"))

# pooling layer:
model.add(MaxPooling2D(pool_size=(pool_size, pool_size)))

model.add(Convolution2D(nb_filters2, conv2_size, conv2_size, border_mode ="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(pool_size, pool_size), dim_ordering='th'))

# Flatten layer - flattens the input, does not affect the batch size:
model.add(Flatten())

# Just your regular densely-connected NN layer:
model.add(Dense(256))
model.add(Activation("relu"))

# Applies Dropout to the input, dropout consists in randomly setting a fraction rate of 
# input units to 0 at each update during training time, which helps prevent overfitting.
model.add(Dropout(0.5))


model.add(Dense(classes_num, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=lr),
              metrics=['accuracy'])

# rescale: rescaling factor. 
# Defaults to None. If None or 0, no rescaling is applied, 
# otherwise we multiply the data by the value provided 
# (after applying all other transformations).

# shear_range: Float. Shear Intensity 
# (Shear angle in counter-clockwise direction in degrees)

# zoom_range: Float or [lower, upper]. 
# Range for random zoom. 
# If a float, [lower, upper] = [1-zoom_range, 1+zoom_range].

# horizontal_flip: Boolean. Randomly flip inputs horizontally.

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

# class_mode: One of "categorical", "binary", "sparse", "input", or None. 
# Default: "categorical". Determines the type of label arrays that are returned:
# "categorical" will be 2D one-hot encoded labels,
# "binary" will be 1D binary labels, "sparse" will be 1D integer labels,
# "input" will be images identical to input images (mainly used to work with autoencoders).
# If None, no labels are returned 
# (the generator will only yield batches of image data, 
# which is useful to use with model.predict_generator()). 
# Please note that in case of class_mode None, 
# the data still needs to reside in a subdirectory of directory for it to work correctly.

train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

# flow_from_directory - takes the path to a directory & generates batches of augmented data.

validation_generator = test_datagen.flow_from_directory(
    validation_data_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

model.fit_generator(
    train_generator,
    samples_per_epoch=samples_per_epoch,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_steps)

# train_generator / validation_generator - x_train, y_train, x_test, y_test;

# steps_per_epoch: Integer or None. Total number of steps (batches of samples) 
# before declaring one epoch finished and starting the next epoch. 
# When training with input tensors such as TensorFlow data tensors, 
# the default None is equal to the number of samples in your dataset 
# divided by the batch size, or 1 if that cannot be determined.

# validation_steps: Only relevant if steps_per_epoch is specified. 
# Total number of steps (batches of samples) to validate before stopping.

model.save('./models/model.h5')
model.save_weights('./models/weights.h5')