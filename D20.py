import random
D20 = range (1, 20)
roll = input ("Type 'roll' to roll the dice: ")
if roll == "roll":
    if random.choice(D20) == 20:
        print ("Critical Success")
    elif random.choice(D20) == 1:
        print ("Critical Failure")
    else:
        print (random.choice(D20))