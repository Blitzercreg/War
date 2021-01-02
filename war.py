import sys, random

title = 'Welcome to War!'
banner = '*' * len(title)
print(banner)
print(title)
print(banner + '\n')

# Score
wins = 0
losses = 0
ties = 0

# Cards
hearts = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 
		'10h', 'Jh', 'Qh', 'Kh', 'Ah']
diamonds = ['2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 
		'10d', 'Jd', 'Qd', 'Kd', 'Ad']
clubs = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 
		'10c', 'Jc', 'Qc', 'Kc', 'Ac']
spades = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
		'10s', 'Js', 'Qs', 'Ks', 'As']

reds = hearts + diamonds
blacks = clubs + spades
deck = blacks + reds

# Create empty list for player and computer
player_deck = []
computer_deck = []

# Shuffle the deck
random.shuffle(deck)

# Deal cards out
for card in range(53):
	if len(deck) > 0:
		player_deck.append(deck[0])
		del deck[0]
		computer_deck.append(deck[0])
		del deck[0]

# Start of game loop
while True:
	# Current score
	score = 'Wins: ' + str(wins) + ' Losses: ' + str(losses) + ' Ties: ' + str(ties)
	print(score)
	print('-' * len(score))

	# Start battle or quit
	key_input = input('Hit enter to battle: ')
	if key_input == 'q':
		sys.exit()

# PLAYERS TURN
	player_card = player_deck[0]

	# Turn players card into a list, detect the suit of the card 
	# and delete the letter part of the card
	_list = list(player_card)
	list_end = len(_list) - 1
	suit = _list[list_end]
	
	if suit == 'h':
		suit = '♥Hearts♥'
	elif suit == 'd':
		suit = '♦Diamonds♦'
	elif suit == 'c':
		suit = '♣Clubs♣'
	elif suit == 's':
		suit = '♠Spades♠'

	del _list[list_end]

	# Turn card back into a string
	player_card = ''
	for i in _list:
	   	player_card += str(i)

	if player_card == 'A' or player_card == '8':
		print("\nYou have drawn an " + str(player_card) + ' of ' + suit)
	else:
		print("\nYou have drawn a " + str(player_card) + ' of ' + suit)

	# Turn the same card into an integer and delete it out of the player deck
	try:
		player_card = int(player_card)
	except ValueError:
		if player_card == 'J':
			player_card = 11
		elif player_card == 'Q':
			player_card = 12
		elif player_card == 'K':
			player_card = 13
		elif player_card == 'A':
			player_card = 14
	del player_deck[0]

# COMPUTERS TURN
	computer_card = computer_deck[0]

	# Turn computers card into a list, detect the suit of the card 
	# and delete the letter part of the card
	_list = list(computer_card)
	list_end = len(_list) - 1
	suit = _list[list_end]
	
	if suit == 'h':
		suit = '♥Hearts♥'
	elif suit == 'd':
		suit = '♦Diamonds♦'
	elif suit == 'c':
		suit = '♣Clubs♣'
	elif suit == 's':
		suit = '♠Spades♠'

	del _list[list_end]

	# Turn card back into a string
	computer_card = ''
	for i in _list:
	   	computer_card += str(i)

	if computer_card == 'A' or computer_card == '8':
		print("The computer has drawn an " + str(computer_card) + ' of ' + (suit))
	else:
		print("The computer has drawn a " + str(computer_card) + ' of ' + (suit))

	# Turn the same card into an integer and delete it out of the computer deck
	try:
		computer_card = int(computer_card)
	except ValueError:
		if computer_card == 'J':
			computer_card = 11
		elif computer_card == 'Q':
			computer_card = 12
		elif computer_card == 'K':
			computer_card = 13
		elif computer_card == 'A':
			computer_card = 14
	del computer_deck[0]

	# Result of battle
	if player_card > computer_card:
		print("\nYou have won the battle, but the war still rages on!\n")
		wins = wins + 1
	elif player_card < computer_card:
		print("\nYou have been bested in this battle, but the war is still going. Don't give up!\n")
		losses = losses + 1
	else:
		print("\nIt has come to a stalemate, who will win the next battle?\n")
		ties = ties + 1

	# End of loop to see if there are anmymore cards
	if wins + losses + ties == 26:
		break
