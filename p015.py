import os
print(os.path.getsize('word.txt'))

sum_size=0
for file in os.listdir('.'):
    if os.path.isfile(file):
        sum_size+=os.path.getsize(file)

print("all size of dir: ",sum_size/1000)

