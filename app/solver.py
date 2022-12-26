from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model
from tensorflow import convert_to_tensor

new_size = (256, 256)

cnn = load_model("../cnn_10f3x3_5f5x5_12l2_15ep_bs15_85.26")

def image_to_matrix(im, resize_size):
    im = ImageOps.grayscale(im.resize(resize_size))
    (w, h) = im.size
    im_pixs = np.array(list(im.getdata())).reshape((w, h)).astype('float32')/255
    return im_pixs

def solve(path):
    im = Image.open(path)
    x = image_to_matrix(im, new_size)
    prediction = cnn.predict(np.array([np.array(convert_to_tensor(x))]))
    return 0 if prediction[0][0] > prediction[0][1] else 1