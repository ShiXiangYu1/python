def is_prime(number: int) -> bool:
    if number in (1,2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True
def print_prime(begin,end):
    for number in range(begin,end+1):
        if is_prime(number): print(f"{number} is prime")
begin=11
end=25
print(begin,end)
