from math import sqrt
from itertools import islice, count, chain

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(list(thousand_primes))
print(sum(islice((x for x in count() if is_prime(x)), 1000)))
print(any(is_prime(x) for x in range(1328, 1361)))
print(all(name == name.title() for name in ['London','Paris','Tokyo']))

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for sun, mon, tue in zip(sunday, monday, tuesday):
    print("average =", (sun + mon + tue) / 2)

temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))
