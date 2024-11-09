import os
import shutil

dir ="./arrange_dir"

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")
    source = f"{dir}/{file}"
    target = f"{dir}/{ext}/{file}"
    shutil.move(source, target)