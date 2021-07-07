import numpy as np

card_names = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
card_values = [1,2,3,4,5,6,7,8,9,10,11,11,11]
user_total,dealer_total = [],[]
sum_user = sum(user_total)
sum_dealer = sum(dealer_total)

test_var = 21

def random_gen():
	return np.random.randint(0,12)

#USER CARD1 AND CARD2
user_c1 = random_gen()
user_card1_value = card_values[user_c1]
user_card1_name = card_names[user_c1]
user_c2 = random_gen()
user_card2_value = card_values[user_c2]
user_card2_name = card_names[user_c2]
user_total.append(user_card1_value)
user_total.append(user_card2_value)
print("Player has card {} and {}\n".format(user_card1_name,user_card2_name))
print("Player's Total : {}\n".format(sum(user_total)))

#DEALER CARD1 AND CARD2
dealer_c1 = random_gen()
dealer_card1_value = card_values[dealer_c1]
dealer_card1_name = card_names[dealer_c1]
dealer_c2 = random_gen()
dealer_card2_value = card_values[dealer_c2]
dealer_card2_name = card_names[dealer_c2]
dealer_total.append(dealer_card1_value)
dealer_total.append(dealer_card2_value)
print("Dealer has card {} and {}\n".format(dealer_card1_name,dealer_card2_name))
print("Dealer's Total : {}\n".format(sum(dealer_total)))

while not sum(user_total) > 21 and not sum(dealer_total) > 21:
	if sum(user_total) == 21 or sum(dealer_total) == 21:
		print("BlackJack")
		break
	else:
		hit_stay = str(input("Hit or stay? \n"))
		if hit_stay.lower() == 'stay':
			if sum(user_total)<sum(dealer_total):
				print("User was stupid. User quits")
				exit()
			while sum(dealer_total)<=sum(user_total) and sum(dealer_total)<22:
				card = random_gen()
				dealer_card = card_values[card]
				dealer_card_name = card_names[card]
				dealer_total.append(dealer_card)
				print("Dealer has card {}".format(dealer_card_name))
				print("Dealer's Total : {}\n".format(sum(dealer_total)))
				if sum(dealer_total)>sum(user_total) and not sum(dealer_total)>21:
					print("Dealer Wins!")
					exit()
			else:
				print("Dealer Bust!")
				print("Player wins.")
				exit()
		else:
			card = random_gen()
			user_card = card_values[card]
			user_card_name = card_names[card]
			user_total.append(user_card)
			print("User has card {}".format(user_card_name))
			print("User's Total : {}\n".format(sum(user_total)))
			# card = random_gen()
			# dealer_card = card_values[card]
			# dealer_card_name = card_names[card]
			# dealer_total.append(dealer_card)
			# print("Dealer has card {}".format(dealer_card_name))
			# print("Dealer's Total : {}\n".format(sum(dealer_total)))

else:
	if sum(user_total)>21:
		print("User bust")
		print("Dealer wins!")
	else:
		print("User wins!")
