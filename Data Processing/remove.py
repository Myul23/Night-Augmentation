import os

base_path = "C://images"
for folder in os.listdir(base_path):
    path = os.path.join(base_path, folder)
    for f in os.listdir(path):
        if len(f.split("_")) > 2:
            # print(f, end=" / ")
            src = os.path.join(path, f)
            os.remove(src)

        # * 이런 형식은 YOLO에 적용되지 않는다.
        # if name[1] in ["gif", "webp", "svg"]:
        #     # print(name[1])
        #     dst = os.path.join(path, f)
        #     os.rename(src, dst)
        #     continue
    print(folder, "finished")
