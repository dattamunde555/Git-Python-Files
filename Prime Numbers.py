# Prime Numbers
# Various uses


import math
##print('The Prime Numbers are:\n2\n3')
primes = [2,3]
index = 0
x = primes[index]
n = 5
primesFile = open('Prime Numbers.txt','w')
primesFile.writelines(['2\n','3\n'])
while n < 1000000:
    while x <= math.sqrt(n) and n % x != 0: # aborts loop if no remainder
        x = primes[index]
        index += 1
        if x > math.sqrt(n):
##            print(n)
            primes.append(n)
            new = str(n) + '\n'
            primesFile.write(new)
    n += 2
    index = 0
    x = primes[index]
primesFile.close()
