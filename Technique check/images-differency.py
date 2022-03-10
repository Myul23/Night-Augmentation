import os

import numpy as np
import cv2

import matplotlib.pyplot as plt


first = "C:/thek9_day.jpg"
second = "C:/thek9_night.jpg"
# first = input("First compare image address: ")
# second = input("Second compare image address: ")
# flag = False
# if not os.path.exists(first):
#     print(f"Adress '{first}' is not valid")
#     flag = True
# if not os.path.exists(second):
#     print(f"Adress '{second}' is not valid")
#     flag = True
# if flag:
#     exit()


morning_base = cv2.imread(first)
night_base = cv2.imread(second)
# morning = cv2.resize(morning_base, (night_base.shape[1], night_base.shape[0]))
# cv2.imwrite("morning.jpg", morning)

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


# * difference in pixel
# _, ax = plt.subplots(3, 4, figsize=(15, 20))
# plt.subplots_adjust(hspace=0.04, wspace=0.04)

# ax[0][0].imshow(morning_base)
# ax[0][0].set_title("morning")
# ax[1][0].imshow(night_base)
# ax[1][0].set_title("night")
# ax[2][0].imshow(different["Gray"], cmap="gray")
# ax[2][0].set_title("GrayScale")
# for i in range(3):
#     ax[i][0].axis("off")

# idx = 1
# for color, channel, order in zip(
#     ["RGB", "HSV", "YCbCr"], [["B", "G", "R"], ["H", "S", "V"], ["Y", "Cr", "Cb"]], [[2, 1, 0], [0, 1, 2], [0, 2, 1]]
# ):
#     for i in range(3):
#         ax[i][idx].imshow(different[color][:, :, order[i]])
#         ax[i][idx].axis("off")
#         ax[i][idx].set_title(f"{''.join(channel)} - {channel[i]}")
#     idx += 1


# * difference as image
# _, ax = plt.subplots(2, 3, figsize=(15, 20))

# i = 0
# for color, code, cidx, channel in zip(["HSV", "YCbCr"], [cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YCrCb], [2, 0], ["V", "Y"]):
#     ax[i][0].boxplot(np.array(different[color][:, :, cidx]).flatten())
#     ax[i][0].set_title(f"difference between morning and night in {color}")
#     morning = cv2.cvtColor(morning_base, code)
#     ax[i][1].hist(np.array(morning[:, :, cidx]).flatten(), bins=25)
#     ax[i][1].set_title(f"{color} - morning {channel} channel")
#     night = cv2.cvtColor(night_base, code)
#     ax[i][2].hist(np.array(night[:, :, cidx]).flatten(), bins=25)
#     ax[i][2].set_title(f"{color} - night {channel} channel")
#     i += 1


# TODO transformation
# python에는 five-number summary가 없다.

# * representation
# _, ax = plt.subplots(2, 4, figsize=(14, 6))
# plt.subplots_adjust(hspace=0.04, wspace=0.04)

# i = 0
# for code, cidx, channel in zip([cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YCrCb], [2, 0], ["V", "Y"]):
#     morning = cv2.cvtColor(morning_base, code)
#     night = cv2.cvtColor(night_base, code)

#     # ax[i][0].hist(np.array(night[:, :, cidx]).flatten(), bins=25)
#     ax[i][0].imshow(night[:, :, cidx], cmap="gray")
#     ax[i][0].axis("off")
#     ax[i][0].set_title(f"original night {channel} channel")

#     # temp = np.array(morning[:, :, cidx]).flatten()
#     temp = morning[:, :, cidx]
#     # ax[i][1].hist(temp, bins=25)
#     ax[i][1].imshow(temp, cmap="gray")
#     ax[i][1].axis("off")

#     temp = np.exp((temp - np.mean(temp)) / np.std(temp))
#     # ax[i][2].hist(temp, bins=25)
#     ax[i][2].imshow(temp, cmap="gray")
#     ax[i][2].axis("off")

#     # ax[i][3].hist(temp * 255 / max(temp), bins=25)
#     ax[i][3].imshow(temp * 255 / np.max(temp.flatten()), cmap="gray")
#     ax[i][3].axis("off")
#     ax[i][3].set_title(f"representation {channel}")
#     i += 1


# * Subtract - Standardization
# img = cv2.cvtColor(morning_base, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(img)

# _, ax = plt.subplots(3, 2, figsize=(15, 20))

# ax[0][0].hist(np.array(v).flatten(), bins=25)
# ax[0][0].set_title("morning V channel")
# ax[0][1].hist(np.array(cv2.split(cv2.cvtColor(night_base, cv2.COLOR_BGR2HSV))[2]).flatten(), bins=25)
# ax[0][1].set_title("night V channel")


# dst = np.add(v, 56).astype(np.uint8)
# ax[1][0].hist(dst.flatten(), bins=25)
# dst = cv2.subtract(dst, 56)
# ax[1][1].hist(dst.flatten(), bins=25)

# dst = np.exp((dst - np.mean(dst)) / np.std(dst))
# ax[2][0].hist(dst.flatten(), bins=25)
# dst = dst * 255 / np.max(dst.flatten())
# ax[2][1].hist(dst.flatten(), bins=25)


# * reverse - Standardization
# img = cv2.cvtColor(morning_base, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(img)

# _, ax = plt.subplots(3, 2, figsize=(10, 14))
# plt.subplots_adjust(hspace=0.04, wspace=0.04)

# # ax[0][0].hist(np.array(v).flatten(), bins=25)
# ax[0][0].imshow(v, cmap="gray")
# ax[0][0].set_title("morning V channel")
# # ax[0][1].hist(np.array(cv2.split(cv2.cvtColor(night_base, cv2.COLOR_BGR2HSV))[2]).flatten(), bins=25)
# ax[0][1].imshow(cv2.split(cv2.cvtColor(night_base, cv2.COLOR_BGR2HSV))[2], cmap="gray")
# ax[0][1].set_title("night V channel")


# dst = np.add(255 - v, 56).astype(np.uint8)
# # ax[1][0].hist(dst.flatten(), bins=25)
# ax[1][0].imshow(dst, cmap="gray")
# dst = cv2.subtract(dst, 56)
# # ax[1][1].hist(dst.flatten(), bins=25)
# ax[1][1].imshow(dst, cmap="gray")

# dst = np.exp((dst - np.mean(dst)) / np.std(dst))
# # ax[2][0].hist(dst.flatten(), bins=25)
# ax[2][0].imshow(dst, cmap="gray")
# dst = dst * 255 / np.max(dst.flatten())
# # ax[2][1].hist(dst.flatten(), bins=25)
# ax[2][1].imshow(dst, cmap="gray")

# for row in range(3):
#     for col in range(2):
#         ax[row][col].axis("off")


plt.show()
