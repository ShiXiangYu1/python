
def read_file():
    result=[]
    with open("./input.txt") as fin:
        for line in fin:
            line=line[:-1]
            result.append(line.split(","))
    return result

def sort_grades(datas):
    return sorted(datas,key=lambda x :int(x[2]),reverse=True)

def write_file(datas):
    with open("./output.txt","w") as fout:
        for data in datas:
            fout.write(",".join(data)+"\n")
datas=read_file()
print("raed_file datas:",datas)
datas=sort_grades(datas)
print("sort_grades datas:",datas)
write_file(datas)
