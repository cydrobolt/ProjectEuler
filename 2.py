a = 1
b = 2
k = 0
A_FOUR_MILLION = 4000000
s = b

while k < A_FOUR_MILLION:
    k = a + b
    a = b
    b = k

    if k % 2 == 0:
        s += k
