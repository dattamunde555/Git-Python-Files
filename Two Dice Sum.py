# Risk Simulator
# Not really a Risk Simulator yet. Just calculates dice roll probabilites.
# Hopefully, will expand to simulate battles in the game of Risk, so as to
# better my knowledge of the chances of winning.

import random
two = three = four = five = six = seven = eight = nine = ten = eleven = twelve = 0
count = 0
while count < 10:
    total = random.randint(1,6) + random.randint(1,6)
    if total == 2:
        two += 1
    elif total == 3:
        three += 1
    elif total == 4:
        four += 1
    elif total == 5:
        five += 1
    elif total == 6:
        six += 1
    elif total == 7:
        seven += 1
    elif total == 8:
        eight += 1
    elif total == 9:
        nine += 1
    elif total == 10:
        ten += 1
    elif total == 11:
        eleven += 1
    elif total == 12:
        twelve += 1
    else:
        break
    count += 1

print('Out of',count,'rolls of two dice, the percentages of each possible sum were:')
print('2:',100*two/count,end='%')
print('\n3:',100*three/count,end='%')
print('\n4:',100*four/count,end='%')
print('\n5:',100*five/count,end='%')
print('\n6:',100*six/count,end='%')
print('\n7:',100*seven/count,end='%')
print('\n8:',100*eight/count,end='%')
print('\n9:',100*nine/count,end='%')
print('\n10:',100*ten/count,end='%')
print('\n11:',100*eleven/count,end='%')
print('\n12:',100*twelve/count,end='%')
