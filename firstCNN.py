import tflearn 
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
from tflearn.data_utils import image_preloader
import numpy as np
import pickle
#https://medium.com/@husseinjaafar/my-first-cnn-in-tflearn-1019f88485f3
#load the data
dataset_file = './dataFirstAttempt.pickle'
data = pickle.load( open(dataset_file, "rb" ) )
#formate it to the proper size
print(data[0])
'''
X, Y = image_preloader(dataset_file, image_shape=(64, 64), mode=’folder’, categorical_labels=True, normalize=True)
X = np.reshape(X, (-1, 64, 64,1))
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()
'''