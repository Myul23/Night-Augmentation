import os
import numpy as np
import matplotlib.pyplot as plt


path = "augmentation"
destination = "result"

if not os.path.exists(path):
    print("No data folder, please check data path")
    exit()


if not os.path.exists(destination):
    os.mkdir(destination)

temp = os.path.join(destination, "train0")
if not os.path.exists(temp):
    os.mkdir(temp)
temp = os.path.join(destination, "train1")
if not os.path.exists(temp):
    os.mkdir(temp)
temp = os.path.join(destination, "test0")
if not os.path.exists(temp):
    os.mkdir(temp)
temp = os.path.join(destination, "test1")
if not os.path.exists(temp):
    os.mkdir(temp)


for folder in os.listdir(path):
    if os.path.isfile(folder) | (".jpg" in folder):
        continue

    folder_path = os.path.join(path, folder)
    # print(folder_path)
    for style in os.listdir(folder_path):
        if os.path.isfile(style) | (".jpg" in folder):
            continue

        style_path = os.path.join(folder_path, style)
        # print(style_path)

        temp = os.listdir(style_path)
        tests = np.random.choice(temp, int(len(temp) * 0.2), replace=False)
        for img in temp:
            if img in tests:
                arg = os.path.join(destination, "test")
            else:
                arg = os.path.join(destination, "train")

            src = os.path.join(style_path, img)
            dst = os.path.join(arg + style, "_".join([folder, img]))
            # print(src, dst)
            os.rename(src, dst)
    print(folder, "finish")
