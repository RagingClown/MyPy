# Nothing to add, just using the well known sum formulas

def sum_difference(n):
    return int((0.5*n*(n+1))**2 - n*(n+1)*(2*n+1)/6)

print(sum_difference(100))