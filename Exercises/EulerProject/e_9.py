# a + b + c = 1000
# a^2 + b^2 = c^2
# a + b >  500
# a < b




# a + b + c = s
# a ^ 2 + b ^ 2 = c ^ 2 (a < b)


import math
def sol(s):
    for a in range(3, s // 4):
        for b in range(s // 4, s // 2):
            if s**2 == 2*s*(a+b) - 2*a*b:
                c = math.sqrt(a**2 +  b**2)
                return [a, b, c]


