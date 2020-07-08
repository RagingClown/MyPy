# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# Even numbers --> 2, 8, 34, 144 -- > E(n) = 4*E(n-1) + E(n-2)

def fibo_sum(upper_bound):
    a = 2
    b = 8
    new_sum = a + b
    c = 4*b + a
    while c < upper_bound:
        new_sum += c
        a = b
        b = c
        c = 4*b + a
    return new_sum

print(fibo_sum(4000000))


