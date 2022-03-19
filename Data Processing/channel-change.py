import os
from glob import glob
import cv2
import matplotlib.pyplot as plt


data_path = "result"

if not os.path.exists(data_path):
    print("No data folder")
    exit()

for address in glob(f"{data_path}/*/*"):
    if "." not in address:
        continue

    img = cv2.imread(address)
    # RGB (BGR) -> BGR (RGB)
    cv2.imwrite(address, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
