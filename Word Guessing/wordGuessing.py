import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'laptop']

pword = []      # word list we will be printing

def guess(char, length):
    
    # print(printchar)
    if char in word1:
        i = 0
        for item in word1:      # for position of char in list
            if char == item:
                pos = i
                break
            i += 1
        pword.pop(pos)  # replacing the char at the index where char is present
        pword.insert(pos, word1[pos])
        word1.pop(pos)      # removing the char from index     for checking if user won or not
        word1.insert(pos, "_")

    for i in range(len(word)):      # printing the list to show user progress
        print(pword[i])



word = random.choice(words)     #gives random word
word1 = []      # new empty list
word1[:0]=word      # entering the random word in list char by char
name = input("Enter you name: ")
print("Good luck!", name)

length = len(word)      # length of word
for i in range(length):
    pword.insert(i, "_")    # Entering char to print the list
turns = 2*length        # turns user have to guess the number
guesses = 0         
# print(word)

print(f"Word length is: {length}")

while guesses<turns:        
    char = input("Guess your word: ").lower()
    guess(char, length)     # calling function
    guesses += 1        # increase no of guesses
    if "_" in pword:        # check if user won the game or it's on going
        pass
    elif "_" not in pword:      # if True then user won
        print(f"Congratulations {name}! You guessed the word right in '{guesses}' guesses.")
        break       # break loop if user won and else statement of loop won't be printed
else:   # USER LOSE if loop is over without break then this statement will execute
    print(f"Oops! {name} You lost. You exceded the guesses.")

