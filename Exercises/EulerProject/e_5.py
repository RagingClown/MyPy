# N - smallest divider; K - Number form 1 to K
# K = 2, N = 2; K = 3, N = 2 * 3; K=4, N = 2 * 3 * 2
# the prime factors of N will be stored in a list


# The function uses a list of the prime factors of the smallest evenly divisible number by 2 to i --> (2,3,4,5,6... i),
# while the range of k are the required numbers. For every i, we will divide it by all its dividers in the list, and
# if the result is bigger than 1, it means we have to add it to the list.
# for i = 2, [2]; for i = 3, [2,3]; for i=4, [2,3,2], since 4 / 2 = 2...

# for k = 10, it returns 2520
# for k = 20, it returns 232792560
# for k = 30, it returns 2329089562800
# for k = 100, it returns 69720375229712477164533808935312303556800


import math

def smallest_d(k):
    prime_factors = [2]
    i = 3
    while i < k:
        factor = i
        for x in range(0, len(prime_factors)):
            if i % prime_factors[x] == 0:
                factor //= prime_factors[x]
        if factor > 1:
            prime_factors.append(factor)
        i += 1
    return math.prod(prime_factors)


print(smallest_d(100))


