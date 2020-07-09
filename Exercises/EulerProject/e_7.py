# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math
def prime(place):
    number = 1
    i = 1 # prime count
    while i < place:
        check = True
        number += 2
        for divider in range(2, math.floor(math.sqrt(number)) + 1):
            if number % divider == 0:
                check = False
                break
        if check:
            i += 1

    return number


print(prime(10001))


