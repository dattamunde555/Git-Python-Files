# Risk Simulator
# Simulates Battles in Risk

import random
battles = 100000
count = 0
attackwin = 0
defensewin = 0
split = 0
while count < battles:
    count += 1
    attack = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    attack.sort(reverse=True)
    defense = [random.randint(1,6),random.randint(1,6)]
    defense.sort(reverse=True)
    if attack[0] > defense[0] and attack[1] > defense[1]:
        attackwin += 1
    elif attack[0] <= defense[0] and attack[1] > defense[1]:
        split += 1
    elif attack[0] > defense[0] and attack[1] <= defense[1]:
        split += 1
    elif attack[0] <= defense[0] and attack[1] <= defense[1]:
        defensewin += 1
    else:
        print('Error.')
        break

print('\nWhen attacker rolls 3 dice, and defender rolls 2, the percentages are:')
print('Attacker wins both: ',100*attackwin/count,'%',sep='')
print('Defender wins both: ',100*defensewin/count,'%',sep='')
print('They each win one: ',100*split/count,'%',sep='')

count = 0
del attack,defense
attackwin = defensewin = split = 0
while count < battles:
    count +=1
    attack = [random.randint(1,6),random.randint(1,6)]
    attack.sort(reverse=True)
    defense = [random.randint(1,6),random.randint(1,6)]
    defense.sort(reverse=True)
    if attack[0] > defense[0] and attack[1] > defense[1]:
        attackwin += 1
    elif attack[0] <= defense[0] and attack[1] > defense[1]:
        split += 1
    elif attack[0] > defense[0] and attack[1] <= defense[1]:
        split += 1
    elif attack[0] <= defense[0] and attack[1] <= defense[1]:
        defensewin += 1
    else:
        print('Error.')
        break

print('\nAttacker rolls 2, defender rolls 2:')
print('Attacker wins both: ',100*attackwin/count,'%',sep='')
print('Defender wins both: ',100*defensewin/count,'%',sep='')
print('They each win one: ',100*split/count,'%',sep='')

count = 0
del attack,defense
attackwin = defensewin = split = 0
while count < battles:
    count += 1
    attack = random.randint(1,6)
    defense = [random.randint(1,6),random.randint(1,6)]
    defense.sort(reverse=True)
    if attack > defense[0]:
        attackwin += 1
    elif attack <= defense[0]:
        defensewin += 1
    else:
        print('Error.')
        break

print('\nAttacker rolls 1, defender rolls 2:')
print('Attacker wins: ',100*attackwin/count,'%',sep='')
print('Defender wins: ',100*defensewin/count,'%',sep='')

count = 0
del attack,defense
attackwin = defensewin = split = 0
while count < battles:
    count += 1
    attack = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    attack.sort(reverse=True)
    defense = random.randint(1,6)
    if attack[0] > defense:
        attackwin += 1
    elif attack[0] <= defense:
        defensewin += 1
    else:
        print('Error.')
        break

print('\nAttacker rolls 3, defender rolls 1:')
print('Attacker wins: ',100*attackwin/count,'%',sep='')
print('Defender wins: ',100*defensewin/count,'%',sep='')

count = 0
del attack,defense
attackwin = defensewin = split = 0
while count < battles:
    count += 1
    attack = [random.randint(1,6),random.randint(1,6)]
    attack.sort(reverse=True)
    defense = random.randint(1,6)
    if attack[0] > defense:
        attackwin += 1
    elif attack[0] <= defense:
        defensewin += 1
    else:
        print('Error.')
        break

print('\nAttacker rolls 2, defender rolls 1:')
print('Attacker wins: ',100*attackwin/count,'%',sep='')
print('Defender wins: ',100*defensewin/count,'%',sep='')
