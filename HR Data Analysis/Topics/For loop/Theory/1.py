list_number = []
while True:
    number = int(input())
    if number < 10:
        continue
    elif number > 100:
        break
    else:
        list_number.append(number)
for i in list_number:
    print(i)