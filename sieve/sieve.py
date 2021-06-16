import math


# True sieve:
def primes(limit: int) -> list[int]:

    sieve = [0, 0] + [1] * (limit - 1)
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = 0

    return [y for x, y in zip(sieve, range(0, limit + 1)) if x]


# naive soln:
# composites = set()
# primes = set(range(2,limit+1))
# for i in range(2,limit//2+1):
#     composites.update(range(i+i,limit+1,i))

# return sorted(primes-composites)
