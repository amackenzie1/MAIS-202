# -*- coding: utf-8 -*-
"""Fingerspell CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bqw8saBhsE636ych2Lf5rkyVDJ9F0EwD
"""

!pip install -q kaggle
from google.colab import files
uploaded = files.upload()

!mkdir ../root/.kaggle
!cp ../content/kaggle.json ../root/.kaggle

!ls ../root/.kaggle

!kaggle datasets download -d grassknoted/asl-alphabet --force

!unzip asl-alphabet.zip

# Commented out IPython magic to ensure Python compatibility.
#[A-Z, del, nothing, space]
import keras
!pip install numpy 
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import os

num_category = 29
all_data = []
# %cd asl_alphabet_train/asl_alphabet_train/A
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../B 
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../C
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
print(len(all_data))

# Commented out IPython magic to ensure Python compatibility.
# %cd ../D
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
print(len(all_data))

# Commented out IPython magic to ensure Python compatibility.
# %cd ../E
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../F
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../G
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../H
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../I
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../J
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../K
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../L
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../M
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../N
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../O
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../P
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../Q
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../R
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../S 
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../T 
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../U
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../V 
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../W
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../X
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../Y 
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../Z
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../'del'
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../nothing
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

# Commented out IPython magic to ensure Python compatibility.
# %cd ../space
for filename in os.listdir("."):
  im = cv2.imread(filename)
  grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  all_data.append([grey, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

import random
import numpy as np
print(len(all_data))
shuffled_data = list(all_data)
random.shuffle(shuffled_data)
smaller_data = shuffled_data[:2000]
X_train = []
y_train = []
for i in smaller_data:
  X_train.append(i[0])
  y_train.append(i[1])


X_train_4D = []
for i in X_train:
  a = []
  for j in i:
    b = []
    for k in j:
      c = []
      c.append(k)
      b.append(c)
    a.append(b)
  X_train_4D.append(a)

X_babyfood = np.array(X_train_4D)
print(X_babyfood.shape)
y_babyfood = np.array(y_train)
print(y_babyfood)



import keras
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

batch_size = 128
num_classes = 29
epochs = 20
input_shape = (200, 200, 1)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


model.fit(X_babyfood, y_babyfood,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1)