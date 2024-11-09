import re

pattern=r"1[3-9]\d{9}"

file_count=""
with open('./datas/phone.txt') as fin:
    file_count=fin.read()

results=re.findall(pattern,file_count)

print(len(results))
for result in results:
    print(result)