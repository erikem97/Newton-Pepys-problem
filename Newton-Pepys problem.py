import random

def dice_throw(number_dice):
    dice = []
    for i in range(number_dice):
        dice.append(random.randrange(1, 7))
    if dice.count(6) >= number_dice/6:
        return 1
    else:
        return 0


number_dice = [6, 12, 18]
number_simulation = 10**6
six_win = 0
twelve_win = 0
eighteen_win = 0

for k in range(number_simulation):
    for i in number_dice:
        if i == 6:
            six_win += dice_throw(i)
        if i == 12:
            twelve_win += dice_throw(i)
        if i == 18:
            eighteen_win += dice_throw(i)
    if k % 10**4 == 0:
        print(((k/number_simulation)*100), '%')


print(six_win/number_simulation, twelve_win/number_simulation, eighteen_win/number_simulation)