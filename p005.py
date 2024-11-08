
def sun_of_square(n):
    result =0
    for number in range(1,n+1):
        result += number**2
    return result


print("sun of square 3:",sun_of_square(3))
print("sun of square 3:",sun_of_square(5))
print("sun of square 3:",sun_of_square(10))