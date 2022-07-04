#Generating our cards::
cards = []
for suit in "CDHS":
	for value in "23456789TJQKA":
		cards.append(suit + value)
				
import random		
hand1 = []
for card in range(13):
	card = random.choice(cards)
	cards.remove(card)
	hand1.append(card)	
print("Hand1:\n",hand1,"\n")

hand2 = []
for card in range(13):
	card = random.choice(cards)
	cards.remove(card)
	hand2.append(card)	
print("Hand2:\n",hand2,"\n")

hand3 = []
for card in range(13):
	card = random.choice(cards)
	cards.remove(card)
	hand3.append(card)	
print("Hand3:\n",hand3,"\n")
hand4 = []
for card in range(13):
	card = random.choice(cards)
	cards.remove(card)
	hand4.append(card)	
print("Hand4:\n",hand4,'\n')

def no_of_cards_suit(hand):
	count_C = 0
	count_D = 0
	count_H = 0
	count_S = 0
	for i in range(13):
		if hand[i][0] == 'C':
			count_C += 1
		if hand[i][0] == 'D':
			count_D += 1
		if hand[i][0] == 'H':
			count_H += 1
		if hand[i][0] == 'S':
			count_S += 1
			
	return count_C,count_D,count_H,count_S	
	
print(no_of_cards_suit(hand1))
print(no_of_cards_suit(hand2))
print(no_of_cards_suit(hand3))
print(no_of_cards_suit(hand4))
print('\n')
			
def arrange_suit_card(hand):
	Hand = []
	for i in range(13):
		if hand[i][0] == 'C':
			Hand.append(hand[i])
	for i in range(13):
		if hand[i][0] == 'D':
			Hand.append(hand[i])
	for i in range(13):
		if hand[i][0] == 'H':
			Hand.append(hand[i])
	for i in range(13):
		if hand[i][0] == 'S':
			Hand.append(hand[i])
	return(Hand)
	
print(arrange_suit_card(hand1))
print(arrange_suit_card(hand2))
print(arrange_suit_card(hand3))
print(arrange_suit_card(hand4))

#How to make ranking of numbers in a suit..
#def ranking('S'):
#	sort_hand = []
#	for i in range(13):
#		if Hand[i][0] == 'S':
#			 for j in range(13):
#			 	if Hand[i][0] == 'K':
#			 		sort_hand.append(Hand[i])
#			 	