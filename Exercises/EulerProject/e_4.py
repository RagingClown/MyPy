def largest_pol():
    max_pol = 0
    a = 100
    while a <= 999:
        b = a
        while b <= 999:
            if is_pol(a * b) and max_pol < a * b:
                max_pol = a * b
            b += 1
        a += 1

    return max_pol


def is_pol(num):
    return str(num) == str(num)[::-1]

print(largest_pol())


def sol2():
    largest_pal = 0
    a = 999
    while a <= 100:
        b = 999
        while a <= b:
            if a * b <= largest_pal:
                break
            if is_pol(a * b):
                largest_pal = a * b
            b -= 1
        a -= 1

