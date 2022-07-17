import random

randomnumber = random.randint(1, 100)   #will give a random random number from 1 to 100
# print(randomnumber)

usernumber = int(input("Enter your guess between 1 to 100: "))
totalguesses = 1        # for current score
while usernumber != randomnumber:
    if usernumber>randomnumber:
        usernumber = int(input("Wrong guess! Please guess a smaller number: "))
    elif usernumber<randomnumber:
        usernumber = int(input("Wrong guess! Please guess a larger number: "))
    totalguesses += 1   
if usernumber == randomnumber:
    print("Congratulations! You guessed it right.")
print(f'Current score is: {totalguesses}')

with open("Python\Mini Projects\The Perfect guess\High Score.txt",'r') as f:  #location of file is based on when this program was programeed
    hiscore = f.read()      # fetch the high score  

# compare high score
if hiscore == '':
    hiscore = str(totalguesses)
    print("Congratulations! You made a new high score.")
elif int(hiscore)<totalguesses:
    print('High score is: ', hiscore)
elif int(hiscore)>totalguesses:
    print("Congratulations! You made a new high score.")
    print(f'Your old high score was {hiscore}')
    hiscore = str(totalguesses)
    with open("Python\Mini Projects\The Perfect guess\High Score.txt",'w') as f:
        f.write(hiscore)        #update high score