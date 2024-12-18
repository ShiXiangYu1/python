

def rtext():
    print("Let's test your programming knowledge.")
    # write your code here]
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    print('Completed, have a nice day!')

    while int(input()) not in range(1, 4):
        print("Please, try again.")
        continue
    print("Congratulations, have a nice day!")

    # print('Please, try again.' if int(input()) in range(1, 5) else 'Congratulations, have a nice day!')


t=rtext()
