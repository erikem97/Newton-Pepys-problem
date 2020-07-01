import random
import matplotlib.pyplot as plt
import math

def dice_throw(number_dice):
    dice = []
    for i in range(number_dice):
        dice.append(random.randrange(1, 7))
    if dice.count(6) >= number_dice/6:
        return 1
    else:
        return 0


number_dice = [6, 12, 18]
number_simulation = 10**2
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






#Caculation of CI

CI_6 = ((1.96)/(number_simulation*math.sqrt(number_simulation)))*(math.sqrt(six_win-(number_simulation-six_win)))*100
CI_12 = ((1.96)/(number_simulation*math.sqrt(number_simulation)))*(math.sqrt(twelve_win-(number_simulation-twelve_win)))*100
CI_18 = ((1.96)/(number_simulation*math.sqrt(number_simulation)))*(math.sqrt(eighteen_win-(number_simulation-eighteen_win)))*100

CI =[CI_6, CI_12, CI_18]
win_rate = [(six_win/number_simulation)*100, (twelve_win/number_simulation)*100, (eighteen_win/number_simulation)*100]
#Prints CI
print(CI)


bar_width = 1.5
plt.bar(number_dice, win_rate, width=bar_width, color='blue', edgecolor='black', yerr=CI, capsize=7)


# general layout



plt.xlabel('Number of dices thrown')
plt.ylabel('Wins [%]')
plt.title('Newton-Pepys problem, simulation')
plt.tight_layout()
plt.show()
