import random
number = []
last = 0
nos = 0
turn = ''
def player_turn():		# player will play their move
	global last

	if last == 20:	# terminate program is 21 will be entered by user
		print("You lost the match. Better luck next time.")
		exit()
	while True:		# take no of digits user wants to enter
		print("Enter how many number you want to enter:")
		global nos
		nos = int(input("> "))
		if nos >= 1 or nos <=3:
			break
		else:
			print("You entered Wrong input please try again")
	
	print("Enter your digits:")
	for i in range(nos):
		try:
			number.append(int(input("> ")))
		except ValueError:		# terminate the program if user enters a string value
			print("You are disqualified for entering wrong input. Good luck next time.")
			exit()
	check_consecutive_number(last+nos)
	if_lose()
	last = number[-1]


def computer_turn():	# computer will play his play
	global last
	global nos
	
	if_lose()


	if turn == 'F':		# if computer has second turn
		for i in range(4-nos):
			number.append(last + i + 1)
		last = number[-1]


	elif turn == 'S':	# if computer has first turn
		if last%4 != 0 and last != 0:
			for i in range(4 - (last % 4)):
				number.append(last+i+1)
		
		elif last%4 == 0 or last == 0:
			for i in range(random.randint(1,3)):	# randomly selects a number between from 1 to 3
				number.append(last + 1 + i)
		last = number[-1]
	
	print("Computer turn...")
	print(number)


def check_consecutive_number(no_range):		# check if numbers are in sequence
	if number[0] == 1:
		for no in range(no_range-1):
			if number[no+1] - number [no] != 1:		# terminate if numbers are not in sequence
				print("You are disqualified for entering wrong input. Good luck next time.")
				exit()
	else:
		print("You are disqualified for entering wrong input. Good luck next time.")
		exit()

def if_lose():		 # check if player lose or not
	global last
	global number
	if last == 20:		#if player enters 21 while 20 was not last number when his turn came this will not word
		print("Congratulations!! you won the game.")
		exit()
	if 21 in number:	# if player also enters 21 along with previous numbers he will lose and in this case last == 20 might not work
		print("Congratulations!! you won the game.")
		exit()


def play():		# start the game
	while True:			# to get who will play first
		print("Choose your turn either first or second (F/S): ")
		global turn
		turn = input("> ").upper()
		if turn == 'F' or turn == 'S':
			break
		else:
			print("Wrong input!! Please try again.")
	
	
	if turn == 'F':		# player chooses first turn
		while True:
			player_turn()
			computer_turn()
	elif turn == 'S':
		while True:		# player chooses second turn
			computer_turn()
			player_turn()
	

if __name__ == "__main__": 		# program main starts from here
	play()