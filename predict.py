import sys
import numpy as np
import matplotlib.pyplot as plt

caffe_root = '/home/jfg/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe

caffe.set_mode_gpu()
model_def = '/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/solver/caffenet_train_val.prototxt'
model_weights = '/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/model_snapshot/caffenet_iter_16315.caffemodel'
IMAGE_FILE = '/home/jfg/Pictures/cat.jpg'

net = caffe.Net(model_def,
                model_weights,
                caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', mu)
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))

net.blobs['data'].reshape(50,
                          3,
                          256, 256)


print('Predict: ', prediction)
print('Class: ', prediction[0].argmax())
