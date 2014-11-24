
# Generates boards of 20 Set Cards without a set in them
# Attempt add to board algorthm

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

def noSet(card, board):
	for cardA in board:
		for cardB in board[board.index(cardA)+1:]:
			if isSet(cardA,cardB,card):
				return False
	return True

def isSet(cardA, cardB, card):
	for i in xrange(4):
		if (cardA[i]+cardB[i]+card[i])%3 !=0:
			return False
	return True
			
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


deck = generateDeck()
board = []

while len(board) < 20:
	board = []
	random.shuffle(deck)
	for card in deck:
		if noSet(card,board):
			board = board + [card]
	
for item in board:	
	print translate(item)



