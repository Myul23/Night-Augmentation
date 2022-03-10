import os
from PIL import Image

path = "./downloads/"
# path = "./1.BBox_manual_labeling/Images/001_box"

# kewords = [
#     "칠성사이다",
#     "생수병",
#     "손소독제",
#     "볼펜",
#     "마우스",
#     "테이크아웃 커피잔",
#     "잼",
#     "와인잔",
#     "유리",
#     "카스",
#     "참치캔",
#     "스위트콘",
#     "신문지",
#     "책",
#     "과자 박스",
#     "색종이",
#     "뽁뽁이",
#     "검은비닐",
#     "비닐",
# ]

kewords = ["스틱 비닐", "클립", "키"]
# kewords = ["스틱 비닐", "키"]

for keword in kewords:
    folder = os.path.join(path, keword)
    # if len(os.listdir(folder)) != 2000:
    #     print(keword + " folder is not enough")

    for idx, f in enumerate(os.listdir(folder)):
        name = f.split(".")
        src = os.path.join(folder, f)
        # img = Image.open(src)
        # if img.size != (500, 500):
        #     img = img.resize((500, 500), Image.ANTIALIAS)

        dst = os.path.join(folder, str(idx) + "." + name[-1])
        os.rename(src, dst)
        # img = img.convert("RGB")
        # img.save(dst)

        # os.remove(src)
        print(f)

# for f in os.listdir(path):
#     # print(f)
#     name = f.split(".")[0]
#     src = os.path.join(path, f)
#     dst = os.path.join(path, name + ".jpg")
#     os.rename(src, dst)
