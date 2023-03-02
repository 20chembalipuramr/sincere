def sp():
	from random import randrange
	from random import randint
	from time import sleep	
	from inputimeout import inputimeout

	computerDeck = []
	playerPile=[]
	computerPile=[]
	playerDeck = []
	suits = ["♥", "♦", "♣", "♠"]
	deck = []
	playerInput="no"
	computerCard = ""
	playerCard = ""
	computerCardDisplayVersion = ""
	playerCardDisplayVersion = ""

	for suit in suits:
		for card in range(1,14):
			if card ==1:
				card = "A"
			elif card == 11:
				card = "J"
			elif card ==12:
				card = "Q"
			elif card == 13:
				card = "K"
			else:
				pass
			cards = (f"{card}{suit}")
			deck.append(cards)

	shuffledDeck=deck
	shuffle(shuffledDeck)

	for i in range (0,25):
		computerDeck.append(shuffledDeck[i])
	print (computerDeck)
	for i in range (26,51):
		playerDeck.append(shuffledDeck[i])
	print (playerDeck)

	print("Your cards have been divided equally and shuffled")
	sleep(1)
	print("When the cards are placed press the enter key if they have the same numerical value, if they do not, then wait for a couple of seconds")
	sleep(1.5)
	print("Now time for the game")

	def round():
		computerCard = ""
		playerCard = ""
		computerCardDisplayVersion = ""
		playerCardDisplayVersion = ""
		computerIndexCard = randrange(0,(len(computerDeck)-1))
		playerIndexCard = randrange(0,len(playerDeck)-1)

		computerCard = computerDeck[computerIndexCard]
		playerCard = playerDeck[playerIndexCard]
		playerPile.append(playerCard)
		computerPile.append(computerCard)
		playerDeck.remove(playerCard)
		computerDeck.remove(computerCard)

		print(f"You place down: {playerCard}")
		print(f"The computer places down a: {computerCard}")
		second = randint(1,3)
		millisecond = randint(1,999)
		randTime = int(f"{second}.{millisecond}")
		playerInput = inputimeout("Is this snap?\n", timeout=randTime)
		computerCardDisplayVersion = computerCard[0:1]
		playerCardDisplayVersion = playerCard[0:1]
		if playerInput == "no" and playerCardDisplayVersion == computerCardDisplayVersion:
			print ("That was a snap, the computer won that round!")
			sleep(1)
			computer_append()
		elif playerInput == "" and playerCardDisplayVersion == computerCardDisplayVersion:
			print ("You got the snap, you won that round!")
			sleep(1)
			player_append()
		elif playerInput == "no" and playerCardDisplayVersion != computerCardDisplayVersion:
			chance = randint(0,10)
			if chance == "7":
				("Oh, it seems the computer messed up and thought it was a snap, you won this round!")
				sleep(1)
				player_append()
			else:
				print ("Good job, that wasn't a snap, nobody won that round!")
				sleep(1)
				round()
		elif playerInput == "" and playerCardDisplayVersion != computerCardDisplayVersion:
			print ("Oof, that wasn't a snap, the computer won that round")
			sleep(1)
			computer_append()

	def computer_append():
		for item in computerPile:
			computerDeck.append(computerPile[item])
			computerPile.remove(computerPile[item])

		
		for item in playerPile:
			computerDeck.append(playerPile[item])
			playerPile.remove(playerPile[item])
		if len(playerDeck) == "0":
			print ("The computer has won!")
			sleep(5)
			exit()
		else:
			round()
	def player_append():
		for item in computerPile:
			playerDeck.append(computerPile[item])
			computerPile.remove(computerPile[item])

		for item in playerPile:
			playerDeck.append(playerPile[item])
			playerPile.remove(playerPile[item])
			if len(computerDeck) == "0":
				print ("The player has won!")
				sleep(5)
				exit()
			else:
				round()
	round()