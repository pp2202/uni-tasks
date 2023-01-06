from ml_utilities import modelRelated as mr
from ml_utilities import dataSet as ds

classes = ds.read_class_info('class_info.txt')
print(classes)
model = mr.read_model('model')

mr.class_check('image-classification/test_images/forest/149.jpg', model, classes)