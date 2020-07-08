# summing all the primes divisible by 3 or 5 below 1000

# mod 3 -- > 3 + 6 + 9... + 999 -- > 3(1 + 2 + 3 + 4 + 5... + 333)
# mod 5 -- > 5(1 + 2 + 3 + 4 + 5 + 6... + 199)
# ---> mod 3 + mod 5 - mod 15 --> p = 999 / divider --> sum = divider * 0.5p(p+1)

def divisible_sum(divider):
    limit = 999
    p = limit // divider
    return  divider * p * (p+1) * 0.5

def primes_sum():
    return divisible_sum(3) + divisible_sum(5) - divisible_sum(15)

print(primes_sum())