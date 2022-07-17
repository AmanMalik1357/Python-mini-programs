# secure a password by converting it into some other symbol or characteres
# generating password with little animation
import os
from time import sleep
secure = (('a', '@'), ('o', '0'), ('and', '&'), ('s', '$'), ('h', '#'), ('p', '%'), ('r', '('), ('b','d'), ('c','3'), ('d','!'), ('g','r'), ('d','*'), ('e','4'), ('m','w'), ('w','m'), ('n','+'), ('l','!'), ('i','1'), ('k','/'),)

def clear():
    if os.name == 'nt':     # for windows os.name is nt
        _ = os.system('cls')

def securepass(password):
    
    for a,b in secure:
        if a in password:
            password = password.replace(a, b)
            
            print(f"Generating your password: {password}")   # print password at every step as it changes
            sleep(0.5)      # wait for 0.5 seconds
            clear()     # will clear the output screen
                        # this all combines and makes a small animation
            
    return password



password = input("Enter you password: ")
clear()

password = securepass(password)
print("Password generated!")
print(f"You secure password is: {password}")