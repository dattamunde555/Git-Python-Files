# Goldbach's Conjecture
# Any even number can be expressed as the sum of two prime numbers


import math
primes = [2,3]
index = 0
x = primes[index]
n = 5
z = 4
while z < 100:
    while z > n:
        while x <= math.sqrt(n) and n % x != 0: # aborts loop if no remainder
            x = primes[index]
            index += 1
            if x > math.sqrt(n):
                primes.append(n)
        n += 2
        index = 0
        x = primes[index]

    while z < n: # z is the even number being tested for goldbachian adherence.
        for i in primes: # cycles through the prime numbers
            for j in primes: # cycles through the prime nubmers
                if j < i: # only tests if j >= i, to prevent checking the same pairs of primes
                    continue
                if i + j == z: # the actual test
                    print(i,'+',j,'=',z)
                    break # breaks out of the j for loop
            if i + j == z:
                break
        if primes[len(primes)-1] == i and i == j and i + j != z:
            # the above conditions are all true only if all pairs of primes have been
            # cycled through, and no pair adds up to z
            print('The number',z,'violates Goldbach\'s Conjecture.')
            break
        z += 2
