import os
import tensorflow as tf
from ml_model import modelCreation as ml
from ml_utilities import dataSet as ds
from ml_utilities import Display as disp
from ml_utilities import modelRelated as mr

tf.get_logger().setLevel('ERROR')

paths = [os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_train/',
os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_test/']

classes = []

train_split = ds.define_split(paths, 0)
test_split = ds.define_split(paths, 1)

ds.gather_class_info(classes, paths)
ds.save_class_info(classes)
ds.list_dataset_details(classes, paths)

disp.display_examples(train_split, classes)

augmented_train_split = mr.augment_data(train_split)

disp.display_examples(augmented_train_split, classes)

model = ml.create_model()

history = model.fit(augmented_train_split, validation_data = test_split, epochs = 128, callbacks = [mr.set_callback(10, 'min', 0.00025)])

disp.plot_history(history)

model.save('model')










