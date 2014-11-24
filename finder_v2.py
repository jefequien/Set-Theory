
# Generates boards of 20 Set Cards without a set in them
# Remove from deck algorithm
# With frequency testing

import random
def generateDeck():
	fulldeck = []
	for i in xrange(3):
		for j in xrange(3):
			for k in xrange(3):
				for l in xrange(3):
					card = [i,j,k,l]
					fulldeck = fulldeck+[card]
	return fulldeck

def findBadCard(cardA, cardB):
	cardC = [0,0,0,0]
	for i in xrange(4):
		if cardA[i] == cardB[i]:
			cardC[i] = cardB[i]
		elif cardA[i] + cardB[i] == 1:
			cardC[i] = 2
		elif cardA[i] + cardB[i] == 2:
			cardC[i] = 1
		elif cardA[i] + cardB[i] == 3:
			cardC[i] = 0
	return cardC

def removeCards(cardA, board, deck):
	for card in board:
		badCard = findBadCard(cardA, card)
		if badCard in deck: deck.remove(badCard)
	return deck

def translate(card):
	word = ""
	for i in xrange(4):
		if i == 0:
			if card[i] == 0:
				word = word + "one,"
			if card[i] == 1:
				word = word + "two,"
			if card[i] == 2:
				word = word + "three,"
		if i == 1:
			if card[i] == 0:
				word = word + "red,"
			if card[i] == 1:
				word = word + "green,"
			if card[i] == 2:
				word = word + "purple,"
		if i == 2:
			if card[i] == 0:
				word = word + "oval,"
			if card[i] == 1:
				word = word + "diamond,"
			if card[i] == 2:
				word = word + "squiggle,"
		if i == 3:
			if card[i] == 0:
				word = word + "hollow"
			if card[i] == 1:
				word = word + "shaded"
			if card[i] == 2:
				word = word + "solid"
	return word



blankdeck = generateDeck()
frequency= [0,0,0,0,0,0,0,0]
board = []

counter = 0
while counter < 10000: #len(board) < 20: 
	board = []
	deck = blankdeck[:]
	random.shuffle(deck)

	while len(deck) > 0:
		card = deck[0]
		deck = removeCards(card, board, deck)
		deck.remove(card)
		board = board + [card]

#	print len(board)

	index = 20 - len(board)
	frequency[index] += 1
	counter+=1
	if counter%1000 == 0:
		print frequency

#for item in board:	
#	print translate(item)


