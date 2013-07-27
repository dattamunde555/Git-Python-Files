# Bubble Sort

import random
L = []

for i in range(10):
    L.append(random.randint(-100, 100))

print('Prior to sorting, L=',L)

#Begin the bubble sort
temp = None
count = 0
while True:
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            count += 1
            temp = L[i+1]
            L[i+1] = L[i]
            L[i] = temp
    print('L=',L)
    if count == 0:
        break
    else:
        print(count,'switches')
        count = 0
        continue
    
