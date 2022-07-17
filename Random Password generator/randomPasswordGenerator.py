# random password generator and saving password in file on desktop and avoiding rewriting of password in same file again and again
# trying to avoid every error possible
import string
import random
import os

# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase
char = string.ascii_letters
digits = string.digits
# symbol = string.punctuation
symbol = "!@#$%()=[]"

# a = string.printable
# b = string.whitespace
# c = a.replace(b,'')

s = char + digits + symbol
s = list(s)

while True:     # for checking the input if it's correct
    try:
        length = int(input("Enter length of password: "))
        if length > 52 or length < 3:
            print("Please enter length of password between 3 to 52.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")
password = "".join(random.sample(s, length))        # random list elements selectes

# random.shuffle(s)         # list items shuffled
# password = "".join(s[0: length])      # saving first few required items of list

print("Password: ",password)        # printing password




while True:
    store = input("Do you want to store password in text file(y/n):")       
    store = store.lower()


    if store == 'n':
        print("Thanks for using our software!")
        break      # exit program in user don't want to save password in file
    elif store == 'y':
        i = 0
        while True:         # checking is the file already exists and if yes then saving password in new file
            fileav = os.path.isfile(f"C:\\Users\\amanm\\Desktop\\Generated Password ({i}).txt")
            if fileav == True:
                i +=1
            elif fileav == False:
                break
        with open(f"C:\\Users\\amanm\\Desktop\\Generated Password ({i}).txt", 'w') as f:        # saving password in new file
            f.write(password)
        print(f"Password saved in file 'Generated Password ({i})' at desktop.")

        break

    else:       # user entered wrong input 
        print("Wrong input!")
