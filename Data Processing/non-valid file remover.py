import os

first = "result"
valid = ["0", "1", "2"]

for f in os.listdir(first):
    second = os.path.join(first, f)
    if os.path.isfile(second) | (f not in valid) | len(f) < 1:
        print(second)
        try:
            os.rmdir(second)
        except:
            os.remove(second)
        continue

    for ff in os.listdir(second):
        third = os.path.join(second, ff)
        print(third)
        if os.path.isfile(third) | (ff not in valid) | len(ff) < 1:
            try:
                os.rmdir(third)
            except:
                os.remove(third)
