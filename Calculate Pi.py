# Calculates pi
# This program calculates digits of pi using circumscribed regular polygons.
# The perimter of the inner and outer polygons converge to the same value
# as the number of sides approaches infinity

# A unit diameter is taken for the circle

import math

tolerance = int(input('How many decimal places of pi would you like to have calculated? '))
places = 0
n = 0
while places < tolerance:
    n += 20 # n is the number of sides of the polygon. n is always even.
    angle = math.radians(180-360/n) # each angle of the regular polygon
    innerC = str(n*math.cos(angle/2))
##    print('Inner perimeter:',innerC)
    # innerC is the perimeter, or circumference, of the inner polygon
    outerC = str(n/math.tan(angle/2))
##    print('Outer perimeter:',outerC)
    # outerC is the perimeter of the outer polygon
    pi = ''
    for i in range(len(innerC)):
        if innerC[i] == outerC[i]:
            pi += innerC[i]
            places = len(pi)-2
        else:
            break
    

pi = float(pi)
print('To',places,'decimal places, pi is:\n',pi)
