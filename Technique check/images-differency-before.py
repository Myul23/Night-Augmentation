import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


first = input("First compare image address: ")
second = input("Second compare image address: ")
flag = False
if not os.path.exists(first):
    print(f"Adress '{first}' is not valid")
    flag = True
if not os.path.exists(second):
    print(f"Adress '{second}' is not valid")
    flag = True
if flag:
    exit()


morning_base = cv2.imread(first)
night_base = cv2.imread(second)


# TODO 0. check differency of two pictures on pixel
different = dict()
for color, code in zip(["Gray", "HSV", "YCbCr"], [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YCrCb]):
    morning = cv2.cvtColor(morning_base, code)
    night = cv2.cvtColor(night_base, code)
    different[color] = cv2.subtract(morning, night)

# // RGB
morning = morning_base.copy()
night = night_base.copy()
different["RGB"] = cv2.subtract(morning, night)


# * use fill (bar graph) - before
_, ax = plt.subplots(4, 3, figsize=(15, 10))
plt.subplots_adjust(hspace=0.3)
for idx, (key, value) in enumerate(different.items()):
    if key == "Gray":
        ax[idx][0].imshow(morning_base)
        ax[idx][1].imshow(night_base)
        ax[idx][0].axis("off")
        ax[idx][1].axis("off")

        ax[idx][2].fill(value)
        ax[idx][2].axes.xaxis.set_visible(False)
        ax[idx][2].set_title(key)
    else:
        for i, (k, v) in enumerate(value.items()):
            ax[idx][i].fill(v)
            ax[idx][i].axes.xaxis.set_visible(False)
            ax[idx][i].set_title(k)

# * use cv2.divide - before
for idx in range(2, 6):
    ax[idx].hist(np.array(np.divide(v, idx * 2)).flatten(), bins=25)
    ax[idx].set_title(f"strength: {idx * 2}")
    ax[idx].set_xlim(0, 255)


plt.show()
