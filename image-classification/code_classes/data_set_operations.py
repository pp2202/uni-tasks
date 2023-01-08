import os
import tensorflow as tf
from random import randrange

def read_class_info(path):
        list = []
        with open('class_info.txt') as f:
            for line in f:
                list.append(line.rstrip())
        return list

def save_class_info(c):
    with open('class_info.txt', 'w') as f:
        for i in c:
            f.write(f"{i}\n")

def gather_class_info(list_name, paths):
    for folder in os.listdir(paths[0]):
        list_name.append(folder)
    print(list_name)

def list_dataset_details(classes, paths):
    for i in classes:
        print(f'Total {i} training images: {len(os.listdir(paths[0] + i))}')
        print(f'Total {i} test images: {len(os.listdir(paths[1] + i))}')

def define_split(paths, i):
    split  = tf.keras.utils.image_dataset_from_directory(paths[i],
        seed = randrange(10,2000))
    return split

