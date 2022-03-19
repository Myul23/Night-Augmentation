import os
import numpy as np
import cv2


data_path = "C://add_crawling"
save_path = "images"

if not os.path.exists(data_path):
    print("No data folder")
    exit()
if not os.path.exists(save_path):
    os.mkdir(save_path)

for folder in os.listdir(data_path):
    base_folder_path = os.path.join(data_path, folder)
    if os.path.isfile(base_folder_path):
        continue

    output_path = os.path.join(save_path, folder)
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    style1 = os.path.join(output_path, "0")
    style2 = os.path.join(output_path, "1")
    if (not os.path.exists(style1)) | (not os.path.exists(style2)):
        os.mkdir(style1)
        os.mkdir(style2)

    for img_file in os.listdir(base_folder_path):
        img_path = os.path.join(base_folder_path, img_file)
        result1 = os.path.join(style1, img_file)
        result2 = os.path.join(style2, img_file)

        img = cv2.imread(img_path)
        cv2.imwrite(result1, img)

        # TODO 만든 데이터 쪽
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # h, s, v = cv2.split(img)

        # dst = np.array(v)
        # dst = np.exp((dst - np.mean(dst)) / np.std(dst))
        # dst = dst * 150 / np.max(dst.flatten())

        # img = cv2.merge((h, s, dst.astype(np.uint8)))
        # img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        # cv2.imwrite(result2, img)

        # TODO crawling 쪽
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img)

        dst = np.add(255 - v, 56).astype(np.uint8)
        dst = cv2.subtract(dst, 56)
        dst = np.exp((dst - np.mean(dst)) / np.std(dst))
        dst = dst * 150 / np.max(dst.flatten())
        dst = np.add(dst, 20)

        img = cv2.merge((h, s, dst.astype(np.uint8)))
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        cv2.imwrite(result2, img)
    print(folder, "finished")
