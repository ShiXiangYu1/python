
import os

data_dir="./datas"
contents=[]
for file in os.listdir(data_dir):
    file_path=os.path.join(data_dir,file)
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path) as fin:
            contents.append(fin.read())

final_content="\n".join(contents)

with open("./datas/text.txt","w") as fout:
    fout.write(final_content)
