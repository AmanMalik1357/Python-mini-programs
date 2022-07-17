# Snake Water Gun    OR    Rock Paper Scissors
import time
import random


def iswin():
    if comp == player:
        return None
    if comp == 's':
        pass
        if player == 'w':
            return False
        elif player == 'g':
            return True
    if comp == 'w':
        pass
        if player == 's':
            return True
        elif player == 'g':
            return False
    if comp == 'g':
        pass
        if player == 's':
            return False
        elif player == 'w':
            return True


print("Computer's turn")
a = random.randint(1, 3)  # random number from 1 to 3
if(a == 1):
    comp = 's'
elif(a == 2):
    comp = 'w'
elif(a == 3):
    comp = 'g'

time.sleep(0.75)    # wait for 0.75 seconds
# player turn
while True:
    print("Your turn: Choose one Snake(s), Water(w) or Gun(g)")
    player = input()
    if player in ['s', 'w', 'g']:
        break
    else:
        print('Wrong input!! Enter again')
        # exit()  # terminate the program if wrong keyword in entered

print(f"\nComputer selected: {comp}")
print(f'You selected: {player}\n')

res = iswin()

if res == None:
    print("The game is tie.")
elif res == True:
    print("Congratulations, You won the game.")
elif res == False:
    print("You loose the game. Better luck next time.")
