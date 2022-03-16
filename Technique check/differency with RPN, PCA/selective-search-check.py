# https://pyimagesearch.com/2020/07/06/region-proposal-object-detection-with-opencv-keras-and-tensorflow/
import numpy as np
import cv2

from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.applications import ResNet50

from tensorflow.keras.models import load_model
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array
from imutils.object_detection import non_max_suppression


# * segmentation 분할을 실시합니다.
def selective_search(image, method="fast"):
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(image)
    if method == "fast":
        ss.switchToSelectiveSearchFast()
    else:
        ss.switchToSelectiveSearchQuality()
    return ss.process()


model = ResNet50(weights="imagenet")
# model = load_model("crawling_transfer_learning_resnet50.h5")
image = cv2.imread("C:/add_crawling/0/5.jpg")
(H, W) = image.shape[:2]


# ? selective search
rects = selective_search(image, "ff")

proposals = []
boxes = []
for (x, y, w, h) in rects:
    if w / float(W) < 0.1 or h / float(H) < 0.1:
        continue

    roi = image[y : y + h, x : x + w]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (224, 224))
    # roi = cv2.resize(roi, (300, 300))
    roi = img_to_array(roi)
    roi = preprocess_input(roi)

    proposals.append(roi)
    boxes.append((x, y, w, h))


preds = model.predict(np.array(proposals))
preds = imagenet_utils.decode_predictions(preds, top=1)
# print(preds)

# * 맞는 box를 붙여봅시다.
# labs = ["stick vinyl", "clip", "key"]
labels = {}
for (i, p) in enumerate(preds):
    # # * softmax
    # prob = np.max(p)
    # # label = labs[p.index(prob)]
    # label = labs[np.where(p == prob)[0][0]]

    (imagenetID, label, prob) = p[0]
    if prob >= 0.5:
        (x, y, w, h) = boxes[i]
        box = (x, y, x + w, y + h)

        L = labels.get(label, [])
        L.append((box, prob))
        labels[label] = L


# * visualization
for label in labels.keys():
    boxes = np.array([p[0] for p in labels[label]])
    proba = np.array([p[1] for p in labels[label]])
    boxes = non_max_suppression(boxes, proba)

    for (startX, startY, endX, endY) in boxes:
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

    cv2.imshow("After", image)
    cv2.waitKey(0)
