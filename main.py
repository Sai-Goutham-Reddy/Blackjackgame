import random
from clear import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, cp_score):
    if user_score == cp_score:
        return " Draw 🙃"
    elif cp_score == 0:
        return "Lose opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return " You went over. You Loose 😭"
    elif cp_score > 21:
        return " Opponent went over. You win 😁"
    elif user_score > cp_score:
        return "You Win 😁"
    else:
        return "You Loose 😭"

def play_game():
    print(logo)
    computer_cards = []
    user_cards = []
    is_game_over = False
    
    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        cp_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if user_score == 0 or cp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_draw = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if user_draw == 'y':
                user_cards.append(deal_card())
            elif user_draw == 'n':
                is_game_over = True
    
    
    while cp_score != 0 and cp_score < 17:
        computer_cards.append(deal_card())
        cp_score = calculate_score(computer_cards)
    
    print(f" Your final hand {user_cards}, final acore: {user_score}")
    print(f" Computer's final hand {computer_cards}, final acore: {cp_score}")
    print(compare(user_score, cp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
    
