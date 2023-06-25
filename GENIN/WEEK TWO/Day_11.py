         #Day 11 practices
     #Blackjack Capstone Project
import random
from typing import List, Any
def deal_card():
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
     card = random.choice(cards)
     return card
def calculate_score(cards):
      user_cards = []
      computer_cards = []
      is_game_over = False
for _ in  range(2):
     computer_cards = []
     new_card = deal_card()
     #user_cards.append(deal_card())
     computer_cards.append(deal_card())
     user_score = calculate_score(deal_card())
     computer_score = calculate_score(computer_cards)
     print(f"your cards: {deal_card()}, current score: {user_score}")
     print(f"computer first card: {computer_cards[0]}")
#


