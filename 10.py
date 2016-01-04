def is_prime(n):
    if n == 0 or n == 1:
        return False
    nlim = int(n ** 0.5)

    for i in xrange(2, nlim+1):
        if n % i == 0:
            # not prime number
            return False
    return True

A_TWO_MILLION = 2000000

sum = 0

for i in xrange(2, A_TWO_MILLION):
    if is_prime(i):
        sum += i

print sum
