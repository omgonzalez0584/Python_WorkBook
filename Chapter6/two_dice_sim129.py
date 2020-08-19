import random as rd
import operator
rolls = {}
roll = 0

for i in range(1000):
    roll = rd.randint(1,6) + rd.randint(1,6)
    if not roll in rolls:
        rolls[roll] = 1
    else:
        rolls[roll] += 1

rolls = dict(sorted(rolls.items(),key=operator.itemgetter(0),reverse=False))

print("Rolls  Times  Simulated Percent")
for key,value in rolls.items():
    print("{:>3} | {:>5} | {:>8.2f}%".format(key,value,(value / 1000)*100))
