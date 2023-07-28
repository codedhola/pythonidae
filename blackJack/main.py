from art import logo
from utils import calculate_score, generate_opening_card


user_cards = []
computer_cards = []

generate_opening_card(user_cards)
generate_opening_card(computer_cards)


print(calculate_score(user_cards))
print(user_cards, computer_cards)