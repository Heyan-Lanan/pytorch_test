import copy
import pickle
import plotly as py
import plotly.express as px
import numpy as np

pyplt = py.offline.plot


def load():
    with open("mnist.pkl", 'rb') as f:
        mnist = pickle.load(f)
    image_0 = copy.deepcopy(mnist["training_images"][0])
    image_0 = image_0.reshape(28, 28)
    # px.imshow(image_0).show()
    pyplt(px.imshow(image_0))
    return mnist["training_images"], mnist["training_labels"], mnist["test_images"], mnist["test_labels"]


load()
# img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#                     [[0, 255, 0], [0, 0, 255], [255, 0, 0]]
#                     ], dtype=np.uint8)
# fig = px.imshow(img_rgb)
# fig.show()
