#Generating our cards::
cards = []
for suit in "CDHS":
	for value in "23456789TJQKA":
		cards.append(suit + value)
		
		
import random		

hand = []
for card in range(13):
	card = random.choice(cards)
	cards.remove(card)
	hand.append(card)
	
print(hand)