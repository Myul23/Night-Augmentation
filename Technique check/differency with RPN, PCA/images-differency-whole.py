import os
from glob import glob

import numpy as np
import cv2

import tensorflow as tf
from sklearn.decomposition import PCA
from tensorflow.keras.applications import VGG16

import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False


# TODO data load
number = 2
small_size = 354
makes = np.random.choice(glob(f"C:/making/{number}/*"), small_size, replace=False)  # 7, 5, 4
crawls = np.random.choice(glob(f"C:/add_crawling/{number}/*"), small_size, replace=False)
# print(makes, crawls)


makes_images = [cv2.imread(address) / 255.0 for address in makes]
makes_shape = makes_images[0].shape

for idx in range(small_size):
    makes_images[idx] = np.reshape(makes_images[idx], (makes_shape[0] * makes_shape[1] * makes_shape[2]))


crawl_images = [cv2.imread(address) / 255.0 for address in crawls]
crawl_shape = crawl_images[0].shape

for idx in range(small_size):
    crawl_images[idx] = np.reshape(crawl_images[idx], (crawl_shape[0] * crawl_shape[1] * crawl_shape[2]))


# print(makes_shape, crawl_shape, np.shape(makes_images), np.shape(crawl_images))
# print(makes_images[0], crawl_images[0])


# TODO PCA on data
makes_pca = PCA(n_components=15, whiten=True)
makes_pca.fit(makes_images)

crawl_pca = PCA(n_components=15, whiten=True)
crawl_pca.fit(crawl_images)

# print(makes_pca.components_, crawl_pca.components_)
# print(makes_pca.mean_, crawl_pca.mean_)
# print(len(makes_pca.mean_) == len(makes_pca.components_[0]))


# ! visualization
for pca, (row, col), img_shape in zip([makes_pca, crawl_pca], [(3, 5), (5, 3)], [makes_shape, crawl_shape]):
    _, axes = plt.subplots(row, col, figsize=(10, 10), subplot_kw={"xticks": (), "yticks": ()})
    for idx, (ax, component) in enumerate(zip(axes.ravel(), pca.components_)):
        component = np.subtract(component, np.min(component))
        component = np.multiply(component, 1 / np.max(component))
        ax.imshow(component.reshape(img_shape))
        ax.set_title(f"{idx + 1}th pc")

plt.show()
