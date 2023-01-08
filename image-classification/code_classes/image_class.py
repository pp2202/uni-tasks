from data_set_operations import read_class_info
from model_operations import read_model, class_check


classes = read_class_info('class_info.txt')
print(classes)
model = read_model('model')

class_check('image-classification/test_images/sea/528.jpg', model, classes)