import os
from PIL import Image
import matplotlib.pyplot as plt

DATADIR = "deep_learning_with_tensorflow_examples/PetImages"
CATEGORIES = ["Dog", "Cat"]

img_path = []

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_path.append(os.path.join(path,img))  # add it to the list of all images

avg_dimension = 0
for img in img_path:
    try:
        im = Image.open(img)
        width, height = im.size
        avg_dimension += width + height
    except:
        print("Error: " + img)

avg_dimension = avg_dimension / len(img_path)
print(avg_dimension)