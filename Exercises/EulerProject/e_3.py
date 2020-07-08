# What is the largest prime factor of the number 600851475143?

#example -- > 45 -- > 3 * 15 -- > 3 * 3 * [5]
import math

def prime_factor(number):
    while number % 2 == 0: # dealing with the unique prime 2
        number /= 2
    n = 3
    while n < math.sqrt(number):
        if number % n == 0:
            number /= n
            n = 3
        n += 2
    return int(number)



