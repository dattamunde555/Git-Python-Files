# Square Root
# Finds the square root of a number

n = float(input('What number would you like to find the square root of? '))
e = 0.001 # epsilon
low = 0
high = max(n,1)
x = (low+high)/2
while abs(x**2-n) > e:
    x = (low+high)/2
    if x**2 == n:
        break
    elif x**2 > n:
        high = x
    elif x**2 < n:
        low = x
print('The square root of',n,'is',x)
