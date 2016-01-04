orig = 600851475143

lim = int(orig ** 0.5)
def is_prime(n):
    nlim = int(n ** 0.5)
    for i in xrange(2, nlim):
        if n % i == 0:
            # not prime number
            return False
    return True

curr_max = 0
for i in xrange(2, lim):
    is_p = is_prime(i)
    if is_p and i > curr_max and orig % i == 0:
        curr_max = i

print curr_max
