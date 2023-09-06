#Billy Boone
#03/12/23
#CS150
#roll allocation for 100 dice rolls

import random #random numbers for dice rolls
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0 #set sum counts to 0

for i in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 2:
        count2 += 1
    elif dice1 + dice2 == 3:
        count3 += 1
    elif dice1 + dice2 == 4:
        count4 += 1
    elif dice1 + dice2 == 5:
        count5 += 1
    elif dice1 + dice2 == 6:
        count6 += 1
    elif dice1 + dice2 == 7:
        count7 += 1
    elif dice1 + dice2 == 8:
        count8 += 1
    elif dice1 + dice2 == 9:
        count9 += 1
    elif dice1 + dice2 == 10:
        count10 += 1
    elif dice1 + dice2 == 11:
        count11 += 1
    elif dice1 + dice2 == 12: #evaluation counts for dice rolls
        count12 += 1
print("2s: ", (count2 * '*')) 
print("3s: ", (count3 * '*'))
print("4s: ", (count4 * '*'))
print("5s: ", (count5 * '*'))
print("6s: ", (count6 * '*'))
print("7s: ", (count7 * '*'))
print("8s: ", (count8 * '*'))
print("9s: ", (count9 * '*'))
print("10s: ", (count10 * '*'))
print("11s: ", (count11 * '*'))
print("12s: ", (count12 * '*')) #multiply count * character
        
        
        
        
        
        
        
